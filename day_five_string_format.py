def valid_template(template: str) -> str:
    """
    Validates the template string.

    Parameters:
    - template (str): The template string to validate.

    Raises:
    - ValueError: If the template is empty.
    - TypeError: If the template is not a string.
    """

    if not template:
        raise ValueError("Template can't be empty")

    if not isinstance(template, str):
        raise TypeError("Template has to be of string type")


def format_message(template: str, **kwargs) -> str:
    """
    Formats a message by filling in the template with provided keyword arguments.

    Parameters:
    - template (str): The template string with placeholders.
    - **kwargs: The keyword arguments to fill the placeholders in the template.

    Returns:
    - str: The formatted message.

    Raises:
    - ValueError: If the template is empty.
    - TypeError: If the template is not a string.
    - KeyError: If a required keyword argument is missing.
    """

    valid_template(template)

    try:
        return template.format(**kwargs)
    except KeyError as e:
        raise KeyError(f"Missing keyword argument: {e}") from e


if __name__ == '__main__':
    # valid test cases
    print(format_message(
        "my name is {name} and I'm of {age}", name="Pratik", age=37))

    print(format_message(
        "abc", name="Pratik", age=37))

    # Invalid test cases
    # print(format_message("", name="Pratik", age=37))
    # print(format_message("my name is {name} and I'm of {age}",))

    # print(format_message(
    #    123, name="Pratik", age=37))

    # print(format_message(
    #     "abc {age} {name} {raja}", name="Pratik", age=37))

    # print(format_message("my name is {name} and age is {age}", name='Raja'))
