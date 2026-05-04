"""Base class for TTS providers

This module defines the abstract base class for Text-to-Speech implementations.
"""

from abc import ABC, abstractmethod
from typing import Optional
import numpy as np


class TTSProvider(ABC):
    """Abstract base class for Text-to-Speech providers"""

    def __init__(
        self,
        rate: int = 150,
        volume: float = 1.0,
        language: str = "es",
    ) -> None:
        """Initialize TTS provider
        
        Args:
            rate: Words per minute
            volume: Volume level (0.0-1.0)
            language: Language code
        """
        self.rate = rate
        self.volume = volume
        self.language = language
    
    @abstractmethod
    async def synthesize(
        self,
        text: str,
    ) -> np.ndarray:
        """Synthesize text to audio
        
        Args:
            text: Text to synthesize
            
        Returns:
            Audio samples as NumPy array
        """
        pass
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the TTS provider"""
        pass
    
    @abstractmethod
    async def cleanup(self) -> None:
        """Cleanup resources"""
        pass


__all__ = ["TTSProvider"]
