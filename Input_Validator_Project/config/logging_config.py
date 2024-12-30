# Constants for log file path and format : logging.py
LOG_FILE_PATH = "logs/app.log"  # Ensure the `logs/` directory exists
ERROR_FILE_PATH = "logs/app_error.log"

LOG_FORMATTER = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_MAX_FILE_SIZE = 10_000
LOG_FILE_BACKUP_COUNT = 3

DEFAULT_LOG_LEVEL = "DEBUG"  # Default log level, can be overridden
