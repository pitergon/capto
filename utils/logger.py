import logging
import os
from logging.handlers import RotatingFileHandler
from utils.variables import (
    LOG_DIR,
    LOG_FILE,
    INFO,
    DEBUG,
    WARNING,
    ERROR,
    CRITICAL
    )


# Ensure the logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Configure Logging
logging.basicConfig(
    level=logging.INFO,  # Default log level
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5),  # Auto-rotating logs
        logging.StreamHandler()  # Log to console as well
    ]
)

# Create a logger instance
logger = logging.getLogger("AI_Agent")

def botlog(message, level=INFO):
    """
    Unified function to log messages at different levels.
    Usage: botlog("Your message", "info" or "warning" or "error" or "debug")
    """
    print(message)

    if level == DEBUG:
        logger.debug(message)
    elif level == INFO:
        logger.info(message)
    elif level == WARNING:
        logger.warning(message)
    elif level == ERROR:
        logger.error(message)
    elif level == CRITICAL:
        logger.critical(message)
    else:
        logger.info(f"Unknown level '{level}': {message}")  # Default to info if incorrect level
