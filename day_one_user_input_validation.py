"""
Day One: Variables, Data Types, Input, Output
"""


def get_valid_name():
    """
    Prompts the user to enter a valid name containing only letters, numbers, and spaces.

    Returns:
        str: The valid name entered by the user.
    """
    while True:
        valid_name = input("Please enter your name: ").strip()
        if valid_name and all(c.isalnum() or c.isspace() for c in valid_name):
            return valid_name
        print("Invalid input. Please enter only letters, numbers, or spaces.")


def get_valid_age():
    """
    Prompts the user to enter a valid age as an integer or float.

    Returns:
        int/float: The valid age entered by the user.
    """
    while True:
        valid_age = input("Please enter your age: ").strip()
        try:
            return float(valid_age) if '.' in valid_age else int(valid_age)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main execution
if __name__ == "__main__":
    name = get_valid_name()
    age = get_valid_age()
    print(f"Hello Mr/Ms {name}, your age is {age}.")
