"""Documentation: API Reference

## Core Classes

### VoiceAgent

Main orchestrator class for the voice agent system.

#### Initialization

```python
agent = VoiceAgent(use_mock=True)
```

**Parameters:**
- `use_mock` (bool): Use mock providers for testing (default: True)

#### Methods

**`async initialize() -> None`**

Initialize all components. Must be called before running the agent.

```python
await agent.initialize()
```

**`async run() -> None`**

Start the main event loop. This is a blocking call that will run until interrupted.

```python
await agent.run()  # Press Ctrl+C to stop
```

**`async cleanup() -> None`**

Cleanup all resources. Automatically called when agent shuts down.

```python
await agent.cleanup()
```

**`async listen_for_speech(duration: float = 5.0) -> Optional[bytes]`**

Listen for audio input for specified duration.

**Parameters:**
- `duration` (float): Duration in seconds to listen

**Returns:**
- `bytes`: Audio data if speech detected, None otherwise

```python
audio = await agent.listen_for_speech(duration=5.0)
```

**`async process_pipeline(audio_data: bytes) -> Optional[str]`**

Process audio through complete STT → LLM → TTS pipeline.

**Parameters:**
- `audio_data` (bytes): Raw audio bytes

**Returns:**
- `str`: AI response text, or None on error

```python
response = await agent.process_pipeline(audio_data)
```

### Microphone

Audio input device interface.

#### Initialization

```python
mic = Microphone(
    sample_rate=16000,
    chunk_size=2048,
    channels=1
)
```

#### Methods

**`async start() -> None`**

Start recording from microphone.

**`async stop() -> None`**

Stop recording and cleanup resources.

**`async read_chunk() -> np.ndarray`**

Read one audio chunk from microphone.

**Returns:**
- `np.ndarray`: Audio samples as int16 array

### Speaker

Audio output device interface.

#### Initialization

```python
speaker = Speaker(sample_rate=16000, channels=1)
```

#### Methods

**`async start() -> None`**

Open speaker for playback.

**`async stop() -> None`**

Close speaker and cleanup resources.

**`async play(audio_data: np.ndarray) -> None`**

Play audio data.

**Parameters:**
- `audio_data` (np.ndarray): Audio samples as int16

## Provider Interfaces

### STTProvider

Abstract base class for Speech-to-Text providers.

#### Methods

**`async transcribe(audio_data: np.ndarray, sample_rate: int = 16000) -> str`**

Transcribe audio to text.

**Parameters:**
- `audio_data` (np.ndarray): Audio samples
- `sample_rate` (int): Sample rate in Hz

**Returns:**
- `str`: Transcribed text

### LLMProvider

Abstract base class for Language Model providers.

#### Methods

**`async generate(prompt: str, temperature: Optional[float] = None, max_tokens: Optional[int] = None) -> str`**

Generate response to prompt.

**Parameters:**
- `prompt` (str): Input text prompt
- `temperature` (float): Sampling temperature override (optional)
- `max_tokens` (int): Maximum tokens override (optional)

**Returns:**
- `str`: Generated response text

### TTSProvider

Abstract base class for Text-to-Speech providers.

#### Methods

**`async synthesize(text: str) -> np.ndarray`**

Synthesize text to audio.

**Parameters:**
- `text` (str): Text to synthesize

**Returns:**
- `np.ndarray`: Audio samples as int16 array

## Configuration

### Environment Variables

All configuration through `.env` file:

```env
# Audio
SAMPLE_RATE=16000              # Hz
CHUNK_SIZE=2048                # samples
CHANNELS=1                     # 1=mono

# APIs
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-3.5-turbo

# Providers
STT_PROVIDER=whisper
LLM_PROVIDER=openai
TTS_PROVIDER=pyttsx3

# Settings
STT_LANGUAGE=es
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=256
TTS_RATE=150
TTS_VOLUME=1.0

# System
OPERATION_TIMEOUT=30
LOG_LEVEL=INFO
DEBUG=False
```

## Examples

### Basic Usage

```python
import asyncio
from src.agent.core import VoiceAgent

async def main():
    agent = VoiceAgent(use_mock=False)
    await agent.initialize()
    await agent.run()

asyncio.run(main())
```

### Custom Providers

```python
from src.agent.core import VoiceAgent
from src.llm.providers import OpenAILLM

agent = VoiceAgent()
agent.llm = OpenAILLM(
    api_key="your-key",
    model="gpt-4",
    temperature=0.5
)
await agent.run()
```

### Single Interaction

```python
agent = VoiceAgent()
await agent.initialize()

# Listen
audio = await agent.listen_for_speech(duration=5.0)

# Process
response = await agent.process_pipeline(audio)
print(f"Response: {response}")

await agent.cleanup()
```

## Error Handling

All async operations may raise exceptions. Wrap in try-except:

```python
try:
    response = await agent.process_pipeline(audio)
except asyncio.TimeoutError:
    print("Operation timed out")
except Exception as e:
    print(f"Error: {e}")
```

## State Machine

Agent states:

- `IDLE`: Ready for input
- `LISTENING`: Capturing audio
- `PROCESSING`: Running pipeline
- `RESPONDING`: Playing response
- `ERROR`: Error state
- `SHUTDOWN`: Shutting down

Access current state:

```python
state = agent.state_machine.current_state
print(f"Current state: {state.value}")
```

## Logging

Enable logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Loggers available:
- `src.agent.core` - Agent operations
- `src.audio.microphone` - Microphone
- `src.audio.speaker` - Speaker
- `src.stt.*` - Speech-to-Text
- `src.llm.*` - Language Model
- `src.tts.*` - Text-to-Speech
"""
