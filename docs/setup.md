"""Documentation: Installation and Setup

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- PortAudio (for audio I/O)

## Step-by-Step Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd voice_agent
```

### 2. Create Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Then edit `.env` with your configuration:

```env
# Audio Configuration
SAMPLE_RATE=16000
CHUNK_SIZE=2048
CHANNELS=1

# API Keys
OPENAI_API_KEY=your-api-key-here

# Provider Selection
STT_PROVIDER=whisper
LLM_PROVIDER=openai
TTS_PROVIDER=pyttsx3

# Model Settings
OPENAI_MODEL=gpt-3.5-turbo
LLM_TEMPERATURE=0.7
TTS_RATE=150

# Logging
LOG_LEVEL=INFO
DEBUG=False
```

## Running the Agent

### Basic Usage

```bash
python src/main.py
```

### Run Examples

```bash
python examples/basic_agent.py
```

### Run Tests

```bash
pytest tests/
```

## Troubleshooting

### PyAudio Installation Issues

**On macOS:**
```bash
brew install portaudio
pip install PyAudio
```

**On Ubuntu/Debian:**
```bash
sudo apt-get install portaudio19-dev
pip install PyAudio
```

**On Windows:**
- Download PyAudio wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
- Install with: `pip install PyAudio-0.2.13-cp310-cp310-win_amd64.whl`

### API Key Issues

Make sure your `.env` file has the correct API keys:
- OpenAI API key should start with `sk-`
- Check that keys are not accidentally committed to git

### Audio Device Issues

List available audio devices:

```python
import pyaudio
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(f"{i}: {p.get_device_info_by_index(i)['name']}")
```

### Debug Mode

Enable debug logging:

```bash
DEBUG=True python src/main.py
```

## Development Setup

For development, install additional dependencies:

```bash
pip install -r requirements.txt[dev]
```

This includes:
- pytest and pytest-asyncio for testing
- black for code formatting
- mypy for type checking
- flake8 for linting

### Code Formatting

```bash
black src/ tests/ examples/
```

### Type Checking

```bash
mypy src/
```

### Running Tests

```bash
pytest tests/ -v
```

## Next Steps

1. Try running the basic example
2. Test with different providers
3. Modify system prompts in config
4. Add custom providers
5. Extend with new features

For more information, see the main README.md and docs/
"""
