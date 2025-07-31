from loguru import logger
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logger.add("logs/blocked.log", rotation="1 MB")
