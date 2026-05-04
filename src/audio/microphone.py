"""Microphone - Audio input device interface

This module handles audio capture from the microphone in a non-blocking,
asynchronous manner using asyncio and PyAudio.
"""

import asyncio
import logging
from typing import Optional
import numpy as np
import pyaudio

from src.config import SAMPLE_RATE, CHUNK_SIZE, CHANNELS, AUDIO_FORMAT

logger = logging.getLogger(__name__)


class Microphone:
    """Asynchronous microphone interface for audio capture"""

    def __init__(
        self,
        sample_rate: int = SAMPLE_RATE,
        chunk_size: int = CHUNK_SIZE,
        channels: int = CHANNELS,
    ) -> None:
        """Initialize microphone interface
        
        Args:
            sample_rate: Sample rate in Hz (default: 16000)
            chunk_size: Chunk size in samples (default: 2048)
            channels: Number of channels (default: 1 for mono)
        """
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.channels = channels
        
        self.pa: Optional[pyaudio.PyAudio] = None
        self.stream: Optional[pyaudio.Stream] = None
        self.is_recording = False
        
        logger.debug(
            f"Microphone initialized: {sample_rate}Hz, "
            f"{chunk_size} samples, {channels} channels"
        )
    
    async def start(self) -> None:
        """Start recording from microphone"""
        if self.is_recording:
            logger.warning("Microphone is already recording")
            return
        
        try:
            self.pa = pyaudio.PyAudio()
            
            # Open microphone stream
            self.stream = self.pa.open(
                format=pyaudio.paInt16,
                channels=self.channels,
                rate=self.sample_rate,
                input=True,
                frames_per_buffer=self.chunk_size,
                exception_on_overflow=False,
            )
            
            self.is_recording = True
            logger.info("Microphone started recording")
            
        except Exception as e:
            logger.error(f"Failed to start microphone: {e}")
            raise
    
    async def stop(self) -> None:
        """Stop recording from microphone"""
        if not self.is_recording:
            logger.warning("Microphone is not recording")
            return
        
        try:
            self.is_recording = False
            
            if self.stream:
                self.stream.stop_stream()
                self.stream.close()
                self.stream = None
            
            if self.pa:
                self.pa.terminate()
                self.pa = None
            
            logger.info("Microphone stopped recording")
            
        except Exception as e:
            logger.error(f"Error stopping microphone: {e}")
            raise
    
    async def read_chunk(self) -> np.ndarray:
        """Read a chunk of audio from microphone
        
        Returns:
            NumPy array of audio samples
        """
        if not self.is_recording or not self.stream:
            raise RuntimeError("Microphone is not recording")
        
        try:
            # Run I/O operation in thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            audio_data = await loop.run_in_executor(
                None,
                self.stream.read,
                self.chunk_size,
                False,  # exception_on_overflow
            )
            
            # Convert bytes to NumPy array
            audio_array = np.frombuffer(audio_data, dtype=np.int16)
            return audio_array
            
        except Exception as e:
            logger.error(f"Error reading from microphone: {e}")
            raise


__all__ = ["Microphone"]
