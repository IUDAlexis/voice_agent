"""Main entry point for Voice Agent"""

import asyncio
import logging
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from config import LOG_LEVEL, LOG_FORMAT, DEBUG, validate_config
from agent.core import VoiceAgent

# Configure logging
logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
)

logger = logging.getLogger(__name__)


async def main() -> None:
    """Main entry point for the voice agent"""
    try:
        logger.info("Starting Voice Agent...")
        
        # Validate configuration
        validate_config()
        logger.debug("Configuration validated")
        
        if DEBUG:
            logger.debug("Debug mode enabled")
        
        # Initialize and run the agent
        agent = VoiceAgent()
        logger.info("Voice Agent initialized")
        
        # Run the agent
        await agent.run()
        
    except KeyboardInterrupt:
        logger.info("Voice Agent interrupted by user")
    except Exception as e:
        logger.exception(f"Error running Voice Agent: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
