from typing import Union, Optional, Dict
from app.validators import validate_input_string, validate_number, validate_student_details
from app.messages import (MARKS_EXIST, ROLL_NO_IN_USE, SUBJECT_NOT_EXIST)
from utils.log_utils.logger import create_logger


logger = create_logger(__name__)


class Student:
    """
    Class representing a student.
    """
    used_roll_number = set()

    def __init__(
            self,
            name: str,
            roll_number: Union[int, float],
            date_of_birth: str,
            gender: str,
            grade: str,
            contact: Optional[str] = None
    ):
        """
        Initialize a student with name, roll number (int or float), date of birth, gender,
        grade, and optional contact.
        """
        logger.info("Intializing student : %s", name)
        # Initialize attributes
        self.name = name
        self.roll_number = roll_number
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.grade = grade
        self.contact = contact
        # dictonary to store subject:marks
        self.academic_record: Dict[str, float] = {}

        validate_student_details({
            "roll_number": self.roll_number,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "grade": self.grade,
            "contact": self.contact,
            "name": self.name
        })
        self._checkup_duplicate_roll_numbers()

    def _checkup_duplicate_roll_numbers(self) -> None:
        """
        Check for duplicate roll numbers
        """
        logger.debug(
            "Veryfing roll number already exists or not: %s", self.roll_number)
        if self.roll_number in self.used_roll_number:
            logger.error("Roll Number %s already in use", self.roll_number)
            raise ValueError(ROLL_NO_IN_USE.format(
                roll_number=self.roll_number))
        self.used_roll_number.add(self.roll_number)
        logger.debug("Registed student %s", self.name)

    def add_marks(self, subject: str, marks: Union[int, float]) -> None:
        """
        Add marks for a subject.
        """
        logger.debug("Adding marks for subject: %s", subject)
        validate_input_string(subject, "Subject Name")
        validate_number(marks, "Marks")

        if subject in self.academic_record:
            logger.error("Marks already exists for this subject: %s", subject)
            raise ValueError(MARKS_EXIST.format(subject=subject))
        self.academic_record[subject] = marks
        logger.debug("Added marks %s for subject %s", marks, subject)

    def update_marks(self, subject: str, marks: Union[int, float]) -> None:
        """
        Update marks for a subject.
        """
        logger.debug("Updating marks for subject: %s", subject)
        validate_input_string(subject, "Subject Name")
        validate_number(marks, "Marks")

        if subject not in self.academic_record:
            logger.error("Marks doesn't exists for this subject: %s", subject)
            raise KeyError(SUBJECT_NOT_EXIST.format(subject=subject))
        self.academic_record[subject] = marks
        logger.debug("Updated marks %s for subject %s", marks, subject)

    def delete_marks(self, subject: str) -> None:
        """
        Delete marks for a subject.
        """
        logger.debug("Deleting marks for subject: %s", subject)
        validate_input_string(subject, "Subject Name")

        if subject not in self.academic_record:
            logger.error("No Marks exists for this subject: %s", subject)
            raise KeyError(SUBJECT_NOT_EXIST.format(subject=subject))
        del self.academic_record[subject]
        logger.debug("Deleted Marks for subject: %s", subject)

    def update_contact(self, contact: str) -> None:
        """
        Update the student's contact information.
        """
        logger.debug("Updating contact details for student: %s", self.name)
        validate_input_string(contact, "Contact")
        self.contact = contact
        logger.debug("Updated contact details for student: %s", self.name)

    def get_details(self) -> Dict:
        """
        Retrieve student details as a dictionary.
        """
        logger.debug("Retrieving details for student %s", self.name)
        details = {
            "Name": self.name,
            "Roll Number": self.roll_number,
            "Date of Birth": self.date_of_birth,
            "Gender": self.gender,
            "Grade": self.grade,
            "Contact": self.contact,
            "Academic record": self.academic_record

        }

        return details
