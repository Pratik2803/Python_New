import os


def file_lister(directory: str = ".") -> None:
    """
    Lists all files in specified directory.

    Arguments:
        directory : The directory to list files from.
                    Defaults to the current directory if not specified

    Returns:
        None. Prints the file names to console
    """

    try:
        for dir_item in os.scandir(directory):
            if dir_item.is_file():
                print(f"File name is {dir_item.name}")
    except FileNotFoundError:
        print(f"Directory {directory} doesn't exists")
    except Exception as e:
        print(f"General error as {e}")


if __name__ == "__main__":
    file_lister(directory="C:\\Users\\prati\\Desktop")
