from app.student_managment_system import StudentManagmentSystem
from app.student import Student
from utils.log_utils.logger import create_logger

logger = create_logger(__name__)

if __name__ == "__main__":
    logger.info("Starting the Student Management System application.")
    student_one = Student(name="Alice", roll_number=1,
                          date_of_birth="2005-06-15", gender="Female", grade="10th")

    student_two = Student(name="Rajat", roll_number=2,
                          date_of_birth="1987-06-15", gender="Female", grade="10th")

    sms = StudentManagmentSystem()

    sms.add_student(student_one)
    sms.add_student(student_two)

    print(sms.get_student_details(roll_number=1))
    sms.update_grade(roll_number=1, new_grade="11th")
    print(sms.get_student_details(roll_number=1))
