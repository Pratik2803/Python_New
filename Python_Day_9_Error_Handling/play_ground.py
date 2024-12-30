class NonNumericInput(Exception):
    """Raises exception for non numeric input"""

    def __init__(self, input, message="Input must be of integer or numeric type"):
        super().__init__(*args)


number = input("Kindly enter a valid number")
