from typing import Optional
from validators.base_validator import BaseValidator
from utils.log_utils.logger import create_logger
from utils.exception_utils.custom_exceptions import ValidationError


logger = create_logger(__name__)


class NumberValidator(BaseValidator):

    """
    Validates whether a given value is a string and satisfies length constraints.

    Attributes:
        min_length (int): Minimum length of the string.
        max_length (int): Maximum length of the string.
    """

    def __init__(self, min_number: Optional[float], max_number: Optional[float]) -> None:
        self.min_number = min_number
        self.max_number = max_number

    def validate(self, value: any) -> bool:

        if not isinstance(value, (int, float)):
            logger.error("Validation Failed: Input %s is not number", value)
            raise ValidationError(f"Validation Failed: {value} is not numeric")

        if self.min_number is not None and value < self.min_number:
            logger.error(
                "Validation Failed: %s is less than minimum allowed number", value)
            raise ValidationError(f"Failed: {value} is less than min.")

        if self.max_number is not None and value > self.max_number:
            logger.error("Validation Failed: %s is more than max", value)
            raise ValidationError(f"{value} is more than maximum")

        logger.info("Validation passed")
        return True
