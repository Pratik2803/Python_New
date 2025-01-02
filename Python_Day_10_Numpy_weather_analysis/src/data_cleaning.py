import numpy as np
from utils.log_utils.logger import create_logger

logging = create_logger(__name__)


class DataCleaning:
    """
    Removes Nan consisting rows from array
    """

    def __init__(self, data: np.ndarray) -> None:
        self.data = data

    def remove_nan_records(self) -> np.ndarray:
        """ Cleans the data by removing rows with NaN values. 

        Returns: 
        np.ndarray: The cleaned data with NaN values removed. """
        logging.info("Cleaning data")
        # Remove rows that contain any NaN values
        clean_data = self.data[~np.isnan(self.data).any(axis=1)]
        logging.info("Data is cleaned")
        return clean_data
