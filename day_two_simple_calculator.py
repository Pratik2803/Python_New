# Function to get valid user input between 1 and 4


def get_number_until_4():
    while True:
        # Clean up input
        user_input = input("Guess a number between 1 and 4: ").strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        try:
            user_input = int(user_input)  # Convert input to integer
            if 1 <= user_input <= 4:  # Check if within valid range
                return user_input
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a valid integer between 1 and 4.")


def add(num_one, num_two):
    return num_one + num_two


def mul(num_one, num_two):
    return num_one * num_two


def sub(num_one, num_two):
    return num_one - num_two


def divide(num_one, num_two):
    return num_one / num_two


def get_number():
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
            whole_number = float(user_input) if '.' in user_input else int(
                user_input)  # Convert to integer
            return whole_number
        except ValueError:
            print("Invalid input. Only whole numbers are accepted. Please try again.")


number_one = get_number()
number_two = get_number()

print("""for add enter 1 
      for subtract enter 2
      for multiply enter 3
      for divide enter 4""")

operation = get_number_until_4()

if operation == 1:
    x = add(number_one, number_two)
elif operation == 2:
    x = sub(number_one, number_two)
elif operation == 3:
    x = mul(number_one, number_two)
elif operation == 4:
    x = divide(number_one, number_two)

print(x)
