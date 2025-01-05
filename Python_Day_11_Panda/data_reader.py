import pandas as pd


class DataReader:
    """
    A class for reading data from CSV files.

    Handles common file reading errors and provides informative messages.
    """

    def __init__(self, filepath: str, sep: str = ",") -> None:
        """
        Initializes the DataReader with the file path and separator.

        Args:
            filepath (str): The path to the CSV file.
            sep (str, optional): The separator used in the CSV file. Defaults to ",".
        """
        self.filepath = filepath
        self.sep = sep

    def read(self) -> pd.DataFrame | None:
        """
        Reads the CSV file and returns a pandas DataFrame.

        Handles FileNotFoundError, EmptyDataError, and ParserError with informative messages.

        Returns:
            pandas.DataFrame or None: The DataFrame if successful, None otherwise.
        """
        try:
            data: pd.DataFrame = pd.read_csv(
                filepath_or_buffer=self.filepath, sep=self.sep)
            return data
        except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
            self._handle_error(e)
        return None  # Return None on error

    @staticmethod
    def _handle_error(e: Exception):
        """ 
        Handles the exceptions raised during file reading. 

        Args: 
            e (Exception): The exception raised. 
        """
        error_messages = {
            FileNotFoundError: "Error: File not found",
            pd.errors.EmptyDataError: "Error: Empty File",
            pd.errors.ParserError: "Error: Not Valid Data"
        }

        print(error_messages[type(e)])
