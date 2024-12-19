import logging
from logging.handlers import RotatingFileHandler


def create_file_handler(file_path, max_file_size, back_up_count, log_fomat, log_level):
    """
    Creates and configures a RotatingFileHandler.

    Args:
        file_path (str): Path to the log file.
        level (str): Log level for the handler.
        formatter (logging.Formatter): Formatter for log messages.
        max_size (int): Maximum file size in bytes before rotation.
        backup_count (int): Number of backup log files to retain.

    Returns:
        RotatingFileHandler: Configured file handler.
    """

    handler = RotatingFileHandler(
        file_path, maxBytes=max_file_size, backupCount=back_up_count)

    handler.setFormatter(logging.Formatter(log_fomat))
    handler.setLevel(log_level)

    return handler


def create_stream_handler(log_format, log_level):
    """
    Creates and configures a StreamHandler for console logging.

    Args:
        level (str): Log level for the handler.
        formatter (logging.Formatter): Formatter for log messages.

    Returns:
        StreamHandler: Configured stream handler.
    """

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(log_format))
    handler.setLevel(log_level)
    return handler
