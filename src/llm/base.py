"""Base class for LLM providers

This module defines the abstract base class for Language Model implementations.
"""

from abc import ABC, abstractmethod
from typing import Optional


class LLMProvider(ABC):
    """Abstract base class for Language Model providers"""

    def __init__(
        self,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: int = 256,
        system_prompt: Optional[str] = None,
    ) -> None:
        """Initialize LLM provider
        
        Args:
            model: Model identifier
            temperature: Sampling temperature (0-2)
            max_tokens: Maximum tokens in response
            system_prompt: System prompt for the model
        """
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.system_prompt = system_prompt or "You are a helpful assistant."
    
    @abstractmethod
    async def generate(
        self,
        prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ) -> str:
        """Generate a response to a prompt
        
        Args:
            prompt: Input prompt
            temperature: Optional override of temperature
            max_tokens: Optional override of max tokens
            
        Returns:
            Generated text response
        """
        pass
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the LLM provider"""
        pass
    
    @abstractmethod
    async def cleanup(self) -> None:
        """Cleanup resources"""
        pass


__all__ = ["LLMProvider"]
