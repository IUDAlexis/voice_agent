"""State management for Voice Agent

This module defines the state machine and state management for the voice agent.
"""

from enum import Enum
from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime


class AgentState(Enum):
    """Agent operational states"""
    IDLE = "idle"  # Waiting for user input
    LISTENING = "listening"  # Recording audio
    PROCESSING = "processing"  # Processing audio through pipeline
    RESPONDING = "responding"  # Generating and playing response
    ERROR = "error"  # Error state
    SHUTDOWN = "shutdown"  # Shutting down


@dataclass
class ConversationTurn:
    """Single turn in a conversation"""
    user_input: Optional[str] = None
    transcribed_text: Optional[str] = None
    ai_response: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    processing_time: float = 0.0
    error: Optional[str] = None


@dataclass
class AgentStateMachine:
    """State machine for voice agent"""
    current_state: AgentState = AgentState.IDLE
    previous_state: AgentState = AgentState.IDLE
    last_turn: Optional[ConversationTurn] = None
    turn_history: list = field(default_factory=list)
    
    def transition(self, new_state: AgentState) -> None:
        """Transition to a new state
        
        Args:
            new_state: The new state to transition to
        """
        self.previous_state = self.current_state
        self.current_state = new_state
    
    def add_turn(self, turn: ConversationTurn) -> None:
        """Add a conversation turn to history
        
        Args:
            turn: Conversation turn to add
        """
        self.last_turn = turn
        self.turn_history.append(turn)
    
    def get_conversation_context(self, max_turns: int = 5) -> str:
        """Get recent conversation context for LLM
        
        Args:
            max_turns: Maximum number of recent turns to include
            
        Returns:
            Formatted conversation context
        """
        recent_turns = self.turn_history[-max_turns:]
        context = []
        
        for turn in recent_turns:
            if turn.user_input:
                context.append(f"User: {turn.user_input}")
            if turn.ai_response:
                context.append(f"Assistant: {turn.ai_response}")
        
        return "\n".join(context)


__all__ = ["AgentState", "ConversationTurn", "AgentStateMachine"]
