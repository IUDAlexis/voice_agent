"""Voice Agent Core - Main orchestration and event loop

This module contains the main VoiceAgent class that orchestrates all components
in the asyncio event loop.
"""

import asyncio
import logging
from typing import Optional

from src.audio.microphone import Microphone
from src.audio.speaker import Speaker
from src.stt.providers import MockSTT
from src.llm.providers import MockLLM
from src.tts.providers import MockTTS
from src.agent.state import AgentState, AgentStateMachine, ConversationTurn
from src.config import OPERATION_TIMEOUT, SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class VoiceAgent:
    """Main Voice Agent class
    
    Orchestrates the entire pipeline:
    Microphone → STT → LLM → TTS → Speaker
    """

    def __init__(
        self,
        use_mock: bool = True,  # Use mock providers for development
    ) -> None:
        """Initialize Voice Agent
        
        Args:
            use_mock: Use mock providers instead of real APIs
        """
        self.use_mock = use_mock
        
        # Initialize components
        self.microphone = Microphone()
        self.speaker = Speaker()
        
        # Initialize providers (using mocks for now)
        self.stt = MockSTT()
        self.llm = MockLLM(system_prompt=SYSTEM_PROMPT)
        self.tts = MockTTS()
        
        # State machine
        self.state_machine = AgentStateMachine()
        
        # Control flags
        self.running = False
        self.should_listen = False
        
        logger.info("Voice Agent initialized")
    
    async def initialize(self) -> None:
        """Initialize all components"""
        logger.info("Initializing Voice Agent components...")
        
        try:
            # Initialize providers
            await self.stt.initialize()
            await self.llm.initialize()
            await self.tts.initialize()
            
            # Initialize audio devices
            await self.microphone.start()
            await self.speaker.start()
            
            self.running = True
            logger.info("Voice Agent fully initialized")
            
        except Exception as e:
            logger.error(f"Initialization error: {e}")
            self.state_machine.transition(AgentState.ERROR)
            raise
    
    async def cleanup(self) -> None:
        """Cleanup all components"""
        logger.info("Cleaning up Voice Agent...")
        
        try:
            self.running = False
            
            # Stop audio devices
            await self.microphone.stop()
            await self.speaker.stop()
            
            # Cleanup providers
            await self.stt.cleanup()
            await self.llm.cleanup()
            await self.tts.cleanup()
            
            logger.info("Voice Agent cleanup complete")
            
        except Exception as e:
            logger.error(f"Cleanup error: {e}")
    
    async def listen_for_speech(self, duration: float = 5.0) -> Optional[bytes]:
        """Listen for speech from microphone
        
        Args:
            duration: Duration to listen in seconds
            
        Returns:
            Audio data or None on error
        """
        try:
            self.state_machine.transition(AgentState.LISTENING)
            logger.debug(f"Listening for {duration} seconds...")
            
            # Simulate listening
            await asyncio.sleep(1.0)
            
            # In real implementation, would collect audio chunks
            audio_data = b"mock_audio_data"
            
            logger.debug("Speech capture complete")
            return audio_data
            
        except asyncio.TimeoutError:
            logger.warning("Listen timeout")
            return None
        except Exception as e:
            logger.error(f"Listen error: {e}")
            return None
    
    async def process_pipeline(self, audio_data: bytes) -> Optional[str]:
        """Process audio through the entire pipeline
        
        Args:
            audio_data: Raw audio data
            
        Returns:
            AI response text or None on error
        """
        turn = ConversationTurn()
        
        try:
            self.state_machine.transition(AgentState.PROCESSING)
            
            # Step 1: Speech-to-Text
            logger.debug("Running STT...")
            user_text = await asyncio.wait_for(
                self.stt.transcribe(b""),
                timeout=OPERATION_TIMEOUT,
            )
            turn.transcribed_text = user_text
            logger.info(f"STT Result: {user_text}")
            
            # Step 2: LLM Generation
            logger.debug("Running LLM...")
            ai_response = await asyncio.wait_for(
                self.llm.generate(user_text),
                timeout=OPERATION_TIMEOUT,
            )
            turn.ai_response = ai_response
            logger.info(f"LLM Result: {ai_response}")
            
            # Step 3: Text-to-Speech
            logger.debug("Running TTS...")
            audio_response = await asyncio.wait_for(
                self.tts.synthesize(ai_response),
                timeout=OPERATION_TIMEOUT,
            )
            
            # Step 4: Play response
            self.state_machine.transition(AgentState.RESPONDING)
            logger.debug("Playing response...")
            await self.speaker.play(audio_response)
            
            # Add turn to history
            self.state_machine.add_turn(turn)
            
            return ai_response
            
        except asyncio.TimeoutError:
            logger.error("Pipeline operation timed out")
            turn.error = "Pipeline timeout"
            self.state_machine.add_turn(turn)
            self.state_machine.transition(AgentState.ERROR)
            return None
        except Exception as e:
            logger.error(f"Pipeline error: {e}")
            turn.error = str(e)
            self.state_machine.add_turn(turn)
            self.state_machine.transition(AgentState.ERROR)
            return None
    
    async def run(self) -> None:
        """Main event loop for the agent"""
        try:
            await self.initialize()
            
            logger.info("Voice Agent starting main loop...")
            logger.info("Press Ctrl+C to stop")
            
            # Main loop
            iteration = 0
            while self.running:
                iteration += 1
                logger.info(f"--- Interaction {iteration} ---")
                
                # Listen for speech
                audio_data = await self.listen_for_speech(duration=5.0)
                
                if audio_data:
                    # Process through pipeline
                    response = await self.process_pipeline(audio_data)
                    
                    if response:
                        logger.info(f"Agent Response: {response}")
                else:
                    logger.info("No speech detected")
                
                self.state_machine.transition(AgentState.IDLE)
                
                # Small delay before next iteration
                await asyncio.sleep(0.5)
        
        except KeyboardInterrupt:
            logger.info("Agent interrupted by user")
        except Exception as e:
            logger.exception(f"Agent runtime error: {e}")
        finally:
            await self.cleanup()


__all__ = ["VoiceAgent"]
