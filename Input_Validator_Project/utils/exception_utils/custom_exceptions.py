class ValidationError(Exception):

    """
    Custom exception raised for validation errors.

    Attributes:
        message (str): Explanation of the validation error.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
