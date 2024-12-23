def read_file(input_file: str) -> str:
    """
    Returns content of a file

    Args:
        input_file : File name with location to read

    Returns:
            The content of the file
    """

    with open(input_file, 'r') as infile:
        return infile.read()


def write_file(output_file: str, data: str) -> None:
    """
    Writes data to a file

    Args:
        out_file : File name with location to write
        data: Text to write to the file

    Returns:
            None
    """

    with open(output_file, 'w') as outfile:
        outfile.write(data)


def reverse_string(text: str) -> str:
    """
    Reverses the string

    Args:
        text: string to be reversed

    Returns:
        Reveresed text as string
    """
    return text[::-1]


def reverse_file(input_file: str, output_file: str) -> None:
    """
    Writes reverse text on input file to output file

    Args:
    input_file: Name of the file data to read
    output_file: Name of the file where reverse data to write
    """

    try:
        content = read_file(input_file)
        reverse_content = reverse_string(content)
        write_file(output_file, reverse_content)

    except FileNotFoundError:
        print(f"Error file : {input_file} not found")

    except Exception as e:
        print(f"An error occured {e}")


if __name__ == '__main__':
    in_file = "Python_Day_8_File_Handling\\log.txt"
    out_file = "Python_Day_8_File_Handling\\rev_log.txt"

    reverse_file(in_file, out_file)
