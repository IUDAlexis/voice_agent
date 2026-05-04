"""Configuration module for Voice Agent

This module contains global configuration settings for the voice agent,
including API keys, audio parameters, and logging settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# AUDIO CONFIGURATION
# ============================================================================

# Audio capture settings
SAMPLE_RATE = int(os.getenv("SAMPLE_RATE", "16000"))  # Hz
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "2048"))  # samples per chunk
CHANNELS = int(os.getenv("CHANNELS", "1"))  # Mono
AUDIO_FORMAT = os.getenv("AUDIO_FORMAT", "int16")  # 16-bit PCM

# ============================================================================
# API CONFIGURATION
# ============================================================================

# OpenAI API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# ============================================================================
# STT CONFIGURATION
# ============================================================================

STT_PROVIDER = os.getenv("STT_PROVIDER", "whisper")  # whisper, google, azure
STT_LANGUAGE = os.getenv("STT_LANGUAGE", "es")  # Spanish by default

# ============================================================================
# TTS CONFIGURATION
# ============================================================================

TTS_PROVIDER = os.getenv("TTS_PROVIDER", "pyttsx3")  # pyttsx3, gtts, azure
TTS_RATE = int(os.getenv("TTS_RATE", "150"))  # Words per minute
TTS_VOLUME = float(os.getenv("TTS_VOLUME", "1.0"))  # 0.0 to 1.0

# ============================================================================
# LLM CONFIGURATION
# ============================================================================

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")  # openai, claude, ollama
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "256"))

# System prompt for the LLM
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "Eres un asistente de voz amable y útil. Responde de forma concisa y clara.",
)

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = os.getenv(
    "LOG_FORMAT",
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# ============================================================================
# AGENT CONFIGURATION
# ============================================================================

# Timeout for agent operations (seconds)
OPERATION_TIMEOUT = int(os.getenv("OPERATION_TIMEOUT", "30"))

# Enable debug mode
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ============================================================================
# VALIDATION
# ============================================================================


def validate_config() -> None:
    """Validate configuration settings"""
    if not OPENAI_API_KEY and LLM_PROVIDER == "openai":
        raise ValueError("OPENAI_API_KEY is required when using OpenAI LLM provider")

    if SAMPLE_RATE not in [8000, 16000, 44100, 48000]:
        raise ValueError(f"Invalid SAMPLE_RATE: {SAMPLE_RATE}")

    if not 0 <= TTS_VOLUME <= 1.0:
        raise ValueError(f"TTS_VOLUME must be between 0 and 1, got {TTS_VOLUME}")


__all__ = [
    "SAMPLE_RATE",
    "CHUNK_SIZE",
    "CHANNELS",
    "AUDIO_FORMAT",
    "OPENAI_API_KEY",
    "OPENAI_MODEL",
    "STT_PROVIDER",
    "STT_LANGUAGE",
    "TTS_PROVIDER",
    "TTS_RATE",
    "TTS_VOLUME",
    "LLM_PROVIDER",
    "LLM_TEMPERATURE",
    "LLM_MAX_TOKENS",
    "SYSTEM_PROMPT",
    "LOG_LEVEL",
    "LOG_FORMAT",
    "OPERATION_TIMEOUT",
    "DEBUG",
    "validate_config",
]
