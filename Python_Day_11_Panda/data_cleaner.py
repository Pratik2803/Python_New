import pandas as pd
from typing import Optional


class DataCleaner:
    """
    Class for cleaning data, such as removing NaN values and duplicates.
    """

    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    def clean_data(self, drop_nan: bool = True, drop_duplicates: bool = True) -> pd.DataFrame:
        """
        Cleans the data by removing NaN values and duplicates based on the specified parameters.

        Args:
            drop_nan (bool): Whether to remove rows with NaN values. Default is True.
            drop_duplicates (bool): Whether to remove duplicate rows. Default is True.

        Returns:
            pd.DataFrame: The cleaned DataFrame.
        """

        if drop_nan:
            self.data.dropna(inplace=True)

        if drop_duplicates:
            self.data.drop_duplicates(inplace=True)

        return self.data

    def save_clean_data(self, file_path: Optional[str] = None) -> None:
        """
        Saves the cleaned data to a specified file path if provided.

        Args:
            file_path (Optional[str]): The file path to save the cleaned data. Default is None.
        """

        if file_path:
            try:
                self.data.to_csv(file_path, index=False)
            except Exception as e:
                print(f"Failed to save file {e}")
