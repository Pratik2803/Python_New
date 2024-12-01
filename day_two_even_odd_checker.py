def get_whole_number():
    """
    Prompt the user to enter a whole number.
    Repeats until the user provides a valid integer input.

    Returns:
        int: A valid whole number entered by the user.
    """
    while True:
        user_input = input("Please enter a whole number: ").strip()
        if not user_input:  # Handle empty input explicitly
            print("Input cannot be empty. Please enter a valid whole number.")
            continue
        try:
            whole_number = int(user_input)  # Convert to integer
            return whole_number
        except ValueError:
            print("Invalid input. Only whole numbers are accepted. Please try again.")


def check_even_or_odd(number):
    """
    Check if a given number is even or odd.

    Args:
        number (int): The number to check.

    Returns:
        str: "even" if the number is even, "odd" otherwise.
    """
    return "even" if number % 2 == 0 else "odd"


if __name__ == "__main__":
    number = get_whole_number()
    result = check_even_or_odd(number)
    print(f"The number {number} is an {result} number.")
