"""Speaker - Audio output device interface

This module handles audio playback to speakers in a non-blocking,
asynchronous manner using asyncio and PyAudio.
"""

import asyncio
import logging
from typing import Optional
import numpy as np
import pyaudio

from src.config import SAMPLE_RATE, CHANNELS, AUDIO_FORMAT

logger = logging.getLogger(__name__)


class Speaker:
    """Asynchronous speaker interface for audio playback"""

    def __init__(
        self,
        sample_rate: int = SAMPLE_RATE,
        channels: int = CHANNELS,
    ) -> None:
        """Initialize speaker interface
        
        Args:
            sample_rate: Sample rate in Hz (default: 16000)
            channels: Number of channels (default: 1 for mono)
        """
        self.sample_rate = sample_rate
        self.channels = channels
        
        self.pa: Optional[pyaudio.PyAudio] = None
        self.stream: Optional[pyaudio.Stream] = None
        self.is_open = False
        
        logger.debug(
            f"Speaker initialized: {sample_rate}Hz, {channels} channels"
        )
    
    async def start(self) -> None:
        """Open speaker for playback"""
        if self.is_open:
            logger.warning("Speaker is already open")
            return
        
        try:
            self.pa = pyaudio.PyAudio()
            
            # Open speaker stream
            self.stream = self.pa.open(
                format=pyaudio.paInt16,
                channels=self.channels,
                rate=self.sample_rate,
                output=True,
                frames_per_buffer=2048,
            )
            
            self.is_open = True
            logger.info("Speaker opened for playback")
            
        except Exception as e:
            logger.error(f"Failed to open speaker: {e}")
            raise
    
    async def stop(self) -> None:
        """Close speaker"""
        if not self.is_open:
            logger.warning("Speaker is not open")
            return
        
        try:
            self.is_open = False
            
            if self.stream:
                self.stream.stop_stream()
                self.stream.close()
                self.stream = None
            
            if self.pa:
                self.pa.terminate()
                self.pa = None
            
            logger.info("Speaker closed")
            
        except Exception as e:
            logger.error(f"Error closing speaker: {e}")
            raise
    
    async def play(self, audio_data: np.ndarray) -> None:
        """Play audio data
        
        Args:
            audio_data: NumPy array of audio samples (int16)
        """
        if not self.is_open or not self.stream:
            raise RuntimeError("Speaker is not open")
        
        try:
            # Convert NumPy array to bytes
            audio_bytes = audio_data.astype(np.int16).tobytes()
            
            # Run I/O operation in thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(
                None,
                self.stream.write,
                audio_bytes,
            )
            
        except Exception as e:
            logger.error(f"Error playing audio: {e}")
            raise


__all__ = ["Speaker"]
