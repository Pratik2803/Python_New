

class Employee:

    """
    A class to represent an employee.
    """

    def __init__(self, emp_id: int, name: str, age: float, salary: float, department: str) -> None:
        """
        Intialize an employee.

        Args:
            emp_id (int) : Unique id for an employee.
            name (str): Full name of the employee.
            age (float): Age of the employee.
            salary (float): Salary of the employee.
            department (str): Department where the employee works.

        Return:
            None
        """

        self._emp_id = emp_id
        self._name = name
        self._age = age
        self._salary = salary
        self._department = department

    @property
    def emp_id(self) -> int:
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value: int) -> None:
        if not value:
            raise ValueError("Employee id can't be empty")
        if not isinstance(value, int):
            raise ValueError("Employee id must be an integer")

        self._emp_id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Employee Name can't be empty")
        if not isinstance(value, str):
            raise ValueError("Employee id must be an string")

        self._name = value

    @property
    def age(self) -> float:
        return self._age

    @age.setter
    def age(self, value: float) -> None:
        if not value:
            raise ValueError("Employee age can't be empty")
        if not isinstance(value, (int, float)):
            raise ValueError("Employee age must be an integer or float")
        if value < 18:
            raise ValueError("Employee age must be 18 or 18+")

        self._age = value

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if not value:
            raise ValueError("Salary can't be empty")
        if not isinstance(value, (int, float)):
            raise ValueError("Salary must be an integer or float")
        if value <= 0:
            raise ValueError("Salary must be +ive")

        self._salary = value

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, value: str) -> None:
        if not value:
            raise ValueError("Department can't be empty")
        if not isinstance(value, str):
            raise ValueError("Department must be String")

        self._department = value

    def __str__(self) -> str:
        """
        Returns a string represenation of employee

        Returns : 
            str : A string represenatation of an employee
        """
        return (f"Employee(ID: {self._emp_id}, Name: {self.name}, Age: {self._age}, "
                f"Salary: {self._salary}, Department: {self._department})")
