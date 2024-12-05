import day_three_constants


def sum_of_numbers():
    """
    Prompts the user to enter a list of numbers (comma-separated or space-separated),
    validates the input, and returns their sum.
    """

    while True:
        user_input = input(day_three_constants.PROMPT_MESSAGE).strip()

        if not user_input:  # Check for empty input
            print(day_three_constants.ERROR_EMPTY_INPUT)
            continue

        try:
            # Normalize input by replacing spaces with commas
            normalized_input = user_input.replace(" ", ",")
            num_list = [float(item)
                        for item in normalized_input.split(',') if item.strip()]
            return sum(num_list)  # Return the sum of the numbers

        except ValueError:
            # Handle invalid inputs like alphabets or improperly formatted numbers
            print(day_three_constants.ERROR_INVALID_INPUT)


# Call the function
if __name__ == "__main__":
    print(day_three_constants.OUTPUT_MESSAGE.format(sum_of_numbers()))
