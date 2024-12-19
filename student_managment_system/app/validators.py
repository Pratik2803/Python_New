from typing import Union
from app.messages import INVALID_NUMBER, INVALID_STRING
from utils.log_utils.logger import create_logger

# Create logger object
logger = create_logger(__name__)


def validate_number(number: Union[int, float], field_name: str) -> None:
    """ Validate the number to ensure it is an integer or float. """
    logger.debug("Validating number for the field %s", field_name)
    if not isinstance(number,  (int, float)):
        logger.error("Validation failed for field %s: %s",
                     field_name, INVALID_NUMBER)
        raise ValueError(INVALID_NUMBER.format(field_name=field_name))


def validate_input_string(value: str, field_name: str) -> None:
    """ Validate that a string input is non-empty and of the correct type. """
    logger.debug("Validating string for the field %s", field_name)
    if not isinstance(value,  str) or not value.strip():
        logger.error("Validation failed for the string %s: %s",
                     field_name, INVALID_STRING)
        raise ValueError(INVALID_STRING.format(field_name=field_name))


def validate_student_details(student_details: dict) -> None:
    """
    Validate input types and values
    """
    logger.debug("Validating student details for student %s",
                 student_details["name"])
    validate_number(student_details["roll_number"], "Roll Number")
    validate_input_string(student_details["name"], "Student Name")
    validate_input_string(student_details["date_of_birth"], "Date of Birth")
    validate_input_string(student_details["gender"], "Gender")
    validate_input_string(student_details["grade"], "Grade")
    if student_details["contact"]:
        validate_input_string(student_details["contact"], "Student Contact")
