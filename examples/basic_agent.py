"""Example: Basic Voice Agent Usage

This example demonstrates the basic usage of the Voice Agent with mock providers.
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agent.core import VoiceAgent


async def main():
    """Run basic voice agent example"""
    print("=== Basic Voice Agent Example ===\n")
    
    # Create agent with mock providers
    agent = VoiceAgent(use_mock=True)
    
    # Run for a few iterations
    try:
        await agent.initialize()
        
        print("Agent initialized. Running 3 interactions...\n")
        
        for i in range(3):
            print(f"--- Interaction {i+1} ---")
            
            # Simulate user input
            print("Listening for speech...")
            audio_data = await agent.listen_for_speech(duration=2.0)
            
            if audio_data:
                response = await agent.process_pipeline(audio_data)
                print(f"Agent: {response}\n")
            else:
                print("No speech detected\n")
        
        print("Example complete!")
        
    finally:
        await agent.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
