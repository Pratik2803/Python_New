from typing import Union


def get_average(*args: Union[int, float]) -> float:
    """Calculate the average of provided numerical values.

        Args:
            *args: A variable number of numeric values (int or float).

        Returns:
            float: The average of the input values.

        Raises:
            ValueError: If no arguments are provided.
    """
    if not args:
        raise ValueError("At least one numeric argument is required.")

    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All arguments must be either int or float.")

    return sum(args)/len(args)


if __name__ == "__main__":

    print(get_average(1))
    print(get_average(1, 2, 3, 4, 5))
