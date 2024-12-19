import logging
from utils.log_utils.log_handlers import create_file_handler, create_stream_handler
from config.logging_config import (
    LOG_FILE_PATH,
    ERROR_FILE_PATH,
    LOG_FORMATTER,
    LOG_MAX_FILE_SIZE,
    LOG_FILE_BACKUP_COUNT,
    DEFAULT_LOG_LEVEL

)


def create_logger(logger_name):
    """
    Create and configure a logger for the application.
    Returns:
        logging.Logger: Configured logger instance.
    """

    # Create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(DEFAULT_LOG_LEVEL)

    # Remove all existing handlers to avoid duplicates in case of multiple logger setups
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create file handler and stream handler

    file_handler = create_file_handler(
        file_path=LOG_FILE_PATH, max_file_size=LOG_MAX_FILE_SIZE, back_up_count=LOG_FILE_BACKUP_COUNT, log_level=DEFAULT_LOG_LEVEL, log_fomat=LOG_FORMATTER)

    error_file_handler = create_file_handler(
        file_path=ERROR_FILE_PATH, max_file_size=LOG_MAX_FILE_SIZE, back_up_count=LOG_FILE_BACKUP_COUNT, log_level=logging.ERROR, log_fomat=LOG_FORMATTER)

    stream_handler = create_stream_handler(
        log_level=DEFAULT_LOG_LEVEL, log_format=LOG_FORMATTER)

    # Add logger to handler
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.addHandler(error_file_handler)

    return logger
