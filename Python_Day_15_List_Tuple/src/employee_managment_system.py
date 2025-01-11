from src.employee import Employee
from typing import List


class EmployeeManagmentSystem:
    """ A class to manage employee records. """

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, emp_id: int, name: str, age: float, salary: float, department: str) -> None:
        """
        Add a new employee to the management system.

        Args:
            emp_id (int): Unique ID for the employee.
            name (str): Full name of the employee.
            age (float): Age of the employee.
            salary (float): Salary of the employee.
            department (str): Department where the employee works.

        Raises:
            ValueError: If an employee with the same ID already exists.

        """
        self._employee_data_validator(emp_id, name, age, salary, department)

        if any([employee.emp_id == emp_id for employee in self.employees]):
            raise ValueError(f"Employee ID: {emp_id} already exists")

        new_employee = Employee(emp_id=emp_id, name=name,
                                age=age, department=department, salary=salary)

        self.employees.append(new_employee)
        print("Employee added succesffuly")

    def _employee_data_validator(self, emp_id: int, name: str, age: float, salary: float, department: str) -> None:
        """
        Validate employee data to ensure it meets system requirements.

        Args:
            emp_id (int): Unique ID for the employee.
            name (str): Full name of the employee.
            age (float): Age of the employee.
            salary (float): Salary of the employee.
            department (str): Department where the employee works.

        Raises:
            ValueError: If any validation fails.
        """
        if not isinstance(emp_id, int) or emp_id <= 0:
            raise ValueError("Employee ID must be +ive integer")

        if not isinstance(name, str) or name.strip():
            raise ValueError("Name must be a non-empty string")

        if not isinstance(age, (int, float)) or age <= 0:
            raise ValueError("Age must be a +ive number")

        if not isinstance(salary, (int, float)) or salary <= 0:
            raise ValueError("Salary must be a +ive number")

        if not isinstance(department, str) or department.strip():
            raise ValueError("Department must be a non-empty string")

    def remove_employee(self, emp_id: int) -> None:
        """
        Remove an employee from managment system.

        Args:
            emp_id(int): Unique ID for the employee

        Raises:
            ValueError: if employee doesn't exists
        """
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"Employee having {emp_id} removed")
                return
        raise ValueError(f"Employee having {emp_id} doesn't exists")

    def update_employee_info(self, emp_id: int, **args) -> None:

        for employee in self.employees:
            if employee.emp_id == emp_id:
                if args['name']:
                    employee.name = args['name']
