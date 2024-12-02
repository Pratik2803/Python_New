def get_positive_integer(prompt):
    """
    Prompts the user for a positive integer greater than 0. Repeats until valid input is provided.
    """
    while True:
        try:
            user_input = int(input(prompt).strip())
            if user_input > 0:
                return user_input
            print("Please enter an integer greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def generate_fibonacci_series(n):
    """
    Generates and prints the Fibonacci series up to `n` terms.
    """
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    for _ in range(n):
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Update numbers for the next term


if __name__ == "__main__":
    num_terms = get_positive_integer(
        "Enter the number of terms for the Fibonacci sequence: ")
    generate_fibonacci_series(num_terms)
