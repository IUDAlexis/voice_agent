"""Base class for STT providers

This module defines the abstract base class for Speech-to-Text implementations.
"""

from abc import ABC, abstractmethod
from typing import Optional
import numpy as np


class STTProvider(ABC):
    """Abstract base class for Speech-to-Text providers"""

    def __init__(self, language: str = "es") -> None:
        """Initialize STT provider
        
        Args:
            language: Language code (default: Spanish)
        """
        self.language = language
    
    @abstractmethod
    async def transcribe(
        self,
        audio_data: np.ndarray,
        sample_rate: int = 16000,
    ) -> str:
        """Transcribe audio to text
        
        Args:
            audio_data: Audio samples as NumPy array
            sample_rate: Sample rate in Hz
            
        Returns:
            Transcribed text
        """
        pass
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the STT provider"""
        pass
    
    @abstractmethod
    async def cleanup(self) -> None:
        """Cleanup resources"""
        pass


__all__ = ["STTProvider"]
