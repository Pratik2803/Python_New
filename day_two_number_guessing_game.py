import random

# Function to get valid user input between 1 and 50


def get_number_until_50():
    while True:
        # Clean up input
        user_input = input("Guess a number between 1 and 50: ").strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        try:
            user_input = int(user_input)  # Convert input to integer
            if 1 <= user_input <= 50:  # Check if within valid range
                return user_input
            else:
                print("Please enter a number between 1 and 50.")
        except ValueError:
            print("Invalid input! Please enter a valid integer between 1 and 50.")

# Function to generate the random number to guess (called once in the game loop)


def number_to_guess():
    return random.randint(1, 50)

# Main game function


def guess_number():
    num_to_guess = number_to_guess()  # Generate the number once
    attempts = 0  # Track the number of attempts

    print("Welcome to the Number Guessing Game! Let's begin.")

    while True:
        user_number = get_number_until_50()  # Get valid user input
        attempts += 1  # Increment the attempts count

        if num_to_guess == user_number:
            # Success message with attempts count
            return f"Correct Guess! You took {attempts} attempts."
        elif user_number > num_to_guess:
            print("Too High!")
        else:
            print("Too Low!")


# Entry point of the program
if __name__ == "__main__":
    result = guess_number()
    print(result)
