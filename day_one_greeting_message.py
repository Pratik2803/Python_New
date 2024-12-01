from day_one_user_input_validation import get_valid_name


def get_greeting_message():
    """
    Prompts the user to input a valid greeting message and ensures that it's not blank.

    Returns:
        str: The valid greeting message entered by the user.
    """
    while True:
        greeting_message = input("Please enter a valid greeting message: ")

        # Check if the input is not blank (empty string)
        if greeting_message.strip():  # strip() removes leading/trailing whitespaces
            return greeting_message

        print("Greeting message can't be blank. Please enter a valid message.")


if __name__ == "__main__":
    # Validate and get a valid name
    name = get_valid_name()

    # Get a valid greeting message from the user
    greeting = get_greeting_message()

    # Print the formatted welcome message
    print(f"Welcome {name}, kindly accept this greeting: {greeting}")
