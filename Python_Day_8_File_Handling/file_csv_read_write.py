import csv


def read_csv(file_path: str) -> list[list[str]]:
    """
    Reads data from a CSV file.

    Args:
        file_path(str) : Path to the input CSV file

    Return:
        Data(list) read from the file.
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

            if not data:
                print(f"File: {file_path} is empty")

            return data

    except FileNotFoundError as e:
        print(f"File: {file_path} not found: {e}")
        return []

    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def modify_data(data: list[list[str]], condition: callable, modifier: callable) -> list[list[str]]:
    """
    Modifies rows of data based on conditions and functions

    Args:
        data(list[list[str]]): Input data to modify

    Return:
        List[List[str]]: Updated data.
    """

    if not data:
        return []

    header = data[0]  # First row is header
    body = data[1:]   # Remaining rows are data

    for row in body:
        if condition(row):
            modifier(row)
    return [header] + body


def write_csv(file_path: str, data: list) -> None:
    """
    Writes data to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        data (list): Data to be written.
    """
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    except Exception as e:
        print(f"Error writing file: {e}")


if __name__ == "__main__":

    # File paths
    input_file = "data.csv"
    output_file = "Updated_data.csv"

    try:
        data = read_csv(input_file)
        # Define modification rules
        condition = lambda row: len(row) > 1 and row[0] == 'Bob'
        modifier = lambda row: row.__setitem__(1, 57)

        # Modify data
        updated_data = modify_data(data, condition, modifier)
        
        # Write data
        write_csv(output_file, updated_data)

    except Exception as e:
        print(f"Processing failed: {e}")
