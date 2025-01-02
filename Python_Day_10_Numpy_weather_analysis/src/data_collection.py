import numpy as np
from utils.log_utils.logger import create_logger

logging = create_logger(__name__)


class DataCollection:
    """ A class to handle data collection from CSV files. """

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def read_csv(self) -> np.ndarray:
        """
        Reads a csv file and Returns the data as Numpy array

        Returns:
            np.ndarray = Data from csv file as Numpy array
        """

        try:
            logging.info("Reading data from %s", self.filepath)
            data = np.genfromtxt(fname=self.filepath,
                                 delimiter=",", skip_header=1)
            logging.info("Read data succesfully from %s", self.filepath)
            return data

        except FileNotFoundError as e:
            logging.error("File %s is not found. Facing error %s",
                          e.filename, e.strerror)
            return np.array([])

        except IOError as e:
            logging.error("Error reading file %s", e.strerror)
            return np.array([])
