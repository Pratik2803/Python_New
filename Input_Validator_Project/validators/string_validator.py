from validators.base_validator import BaseValidator
from utils.log_utils.logger import create_logger
from utils.exception_utils.custom_exceptions import ValidationError
from config.validators_config import (MIN_STRING_LENGTH,
                                      MAX_STRING_LENGTH)


logger = create_logger(__name__)


class StringValidtor(BaseValidator):

    """
    Validates whether a given value is a string and satisfies length constraints.

    Attributes:
        min_length (int): Minimum length of the string.
        max_length (int): Maximum length of the string.
    """

    def __init__(self, min_length: int = MIN_STRING_LENGTH, max_length: int = MAX_STRING_LENGTH) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value: any) -> bool:

        if not isinstance(value, str):
            logger.error(
                "Validation Failed: provided value %s is not string", value)
            raise ValidationError("Value must be string")

        if not (self.min_length <= len(value) <= self.max_length):
            logger.error("Validation Failed: Lenth must be between %s and %s",
                         self.min_length, self.max_length)
            raise ValidationError(
                "String Length Must be between {self.min_length} and {self.max_length}")

        return True
