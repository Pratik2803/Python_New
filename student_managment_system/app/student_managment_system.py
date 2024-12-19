from utils.log_utils.logger import create_logger
from app.student import Student

logger = create_logger(__name__)


class StudentManagmentSystem:

    def __init__(self):
        self.students = {}  # Key: roll_number, Value: Student object
        logger.info("Student Management System initialized.")

    def add_student(self, student: Student) -> None:
        if student.roll_number in self.students:
            logger.error(
                "Student with roll number %s already exists", student.roll_number)

            raise ValueError(f"Student having roll number {
                             student.roll_number} already exists")

        self.students[student.roll_number] = student
        logger.info("Student added : %s , Roll No: %s",
                    student.name, student.roll_number)

    def remove_student(self, roll_number) -> None:
        if roll_number not in self.students:
            logger.error(
                "No student found with this roll number: %s", roll_number)
            raise ValueError(
                f"No student found with this roll number: {roll_number}")

        del self.students[roll_number]
        logger.info("Student removed: Roll No: %s", roll_number)

    def get_student_details(self, roll_number) -> dict:
        if roll_number not in self.students:
            logger.error(
                "No student found with this roll number: %s", roll_number)
            raise ValueError(
                f"No student found with this roll number: {roll_number}")

        logger.info("Fetched student details: Roll No: %s", roll_number)
        return self.students[roll_number].get_details()

    def update_grade(self, roll_number, new_grade):
        if roll_number not in self.students:
            logger.error(
                "No student found with this roll number: %s", roll_number)
            raise ValueError(
                f"No student found with this roll number: {roll_number}")

        self.students[roll_number].grade = new_grade
        logger.info("Student : %s, Roll Number: %s, New Grade is: %s",
                    self.students[roll_number].name, self.students[roll_number].roll_number, self.students[roll_number].grade)
