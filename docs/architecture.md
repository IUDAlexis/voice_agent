"""Documentation: System Architecture

## Overview

The Voice Agent is a conversational speech interface built with pure Python and asyncio.
It implements a real-time pipeline for voice interaction.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        VOICE AGENT                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │          │    │          │    │          │    │          │  │
│  │Microphone├──▶ │   STT    ├──▶ │   LLM    ├──▶ │   TTS    │  │
│  │          │    │          │    │          │    │          │  │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  │
│                                                        │          │
│                                                        ▼          │
│                                                   ┌──────────┐   │
│                                                   │          │   │
│                                                   │ Speaker  │   │
│                                                   │          │   │
│                                                   └──────────┘   │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │         Event Loop (asyncio)                             │   │
│  │  Coordinates all operations in non-blocking manner       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Components

### 1. Audio Module (`src/audio/`)

**Microphone**: Captures audio from the microphone in real-time
- Runs in asyncio thread pool to avoid blocking
- Configurable sample rate, chunk size
- Returns audio as NumPy arrays

**Speaker**: Plays audio responses
- Runs in asyncio thread pool
- Manages PyAudio stream
- Handles volume control

### 2. STT Module (`src/stt/`)

**Speech-to-Text (STT)**: Converts audio to text
- Abstract base class for provider implementations
- Implementations: Whisper, Google, Azure
- Default: OpenAI Whisper

### 3. LLM Module (`src/llm/`)

**Language Model (LLM)**: Generates conversational responses
- Abstract base class for provider implementations
- Implementations: OpenAI, Claude, Ollama
- Maintains conversation context

### 4. TTS Module (`src/tts/`)

**Text-to-Speech (TTS)**: Converts text to audio
- Abstract base class for provider implementations
- Implementations: pyttsx3, Google TTS, Azure TTS
- Returns audio as NumPy arrays

### 5. Agent Module (`src/agent/`)

**VoiceAgent**: Main orchestrator
- Manages the event loop
- Coordinates all components
- Handles state transitions

**State Machine**: Tracks agent state
- IDLE: Ready for input
- LISTENING: Capturing audio
- PROCESSING: Running pipeline
- RESPONDING: Playing response
- ERROR: Error state

## Event Loop Design

The agent uses `asyncio` for non-blocking, concurrent operations:

```python
async def main():
    agent = VoiceAgent()
    await agent.initialize()
    
    while agent.running:
        # Listen for speech (non-blocking)
        audio = await agent.listen_for_speech()
        
        # Process through pipeline (non-blocking)
        response = await agent.process_pipeline(audio)
        
        # Play response (non-blocking)
        await agent.speaker.play(response)
```

## Data Flow

1. **Audio Capture**: Microphone captures raw audio chunks
2. **STT Processing**: Audio converted to text
3. **LLM Generation**: Text processed by language model
4. **TTS Synthesis**: Response converted back to audio
5. **Playback**: Audio played through speaker

## Latency Optimization

- All I/O operations run in thread pool
- Concurrent processing where possible
- Configurable timeouts for all operations
- Buffer management for smooth audio flow

## Error Handling

- Try-catch around each component
- Graceful degradation on errors
- State transitions on failures
- Logging of all errors for debugging

## Configuration

All parameters are configurable via environment variables (`.env` file):
- Audio parameters (sample rate, chunk size)
- API keys and model selection
- TTS/STT settings
- LLM parameters (temperature, max tokens)
- Logging levels

## Future Enhancements

- [ ] Multi-turn context window
- [ ] Interrupt detection
- [ ] Parallel component processing
- [ ] Custom provider plugins
- [ ] WebSocket support for remote clients
- [ ] Audio compression
- [ ] Multi-language support
- [ ] Voice activity detection (VAD)
"""
