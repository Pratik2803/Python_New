def get_rectangle_height():
    """
    Prompts the user to enter a valid height for the rectangle.
    Ensures the input is a valid number (either integer or float).
    """
    while True:
        height_input = input("Enter rectangle height (positive number): ")
        try:
            # Check if the number is a positive float or int
            height = float(height_input) if '.' in height_input else int(
                height_input)
            if height <= 0:
                print("Height must be a positive number. Please try again.")
                continue
            return height
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_rectangle_width():
    """
    Prompts the user to enter a valid width for the rectangle.
    Ensures the input is a valid number (either integer or float).
    """
    while True:
        width_input = input("Enter rectangle width (positive number): ")
        try:
            # Check if the number is a positive float or int
            width = float(width_input) if '.' in width_input else int(
                width_input)
            if width <= 0:
                print("Width must be a positive number. Please try again.")
                continue
            return width
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_rectangle_area(height, width):
    """
    Calculates the area of the rectangle.
    Formula: area = height * width
    """
    return height * width


if __name__ == "__main__":
    # Get height and width from the user
    rectangle_height = get_rectangle_height()
    rectangle_width = get_rectangle_width()

    # Calculate area
    rectangle_area = get_rectangle_area(rectangle_height, rectangle_width)

    # Print the result
    print(f"Rectangle area is {rectangle_area}")
