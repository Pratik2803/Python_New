import re
from validators.base_validator import BaseValidator
from utils.log_utils.logger import create_logger
from utils.exception_utils.custom_exceptions import ValidationError


logger = create_logger(__name__)


class EmailValidtor(BaseValidator):
    """
    Validates whether a given value is a valid email address.

    Attributes:
        EMAIL_REGEX (str): Regular expression for email validation.
    """

    EMAIL_REGEX: str = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    def validate(self, value: any) -> bool:

        if not isinstance(value, str):
            logger.error("%s is not a valid email", value)
            raise ValidationError(f"{value} is not a valid email")

        if not re.match(pattern=self.EMAIL_REGEX, string=value):
            logger.error("%s is not a valid email", value)
            raise ValidationError(f"{value} is not a valid email")

        logger.info("Email validation passed")
        return True
