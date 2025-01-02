import numpy as np


class DataAnalysis:
    """
    A class to handle data analysis operations.
    """

    def analyze_data(self, data: np.ndarray) -> dict:
        """
        Analyzes the data and returns a dictionary with statistical measures.

        Args:
            data (np.ndarray): The cleaned data as a NumPy array.

        Returns:
            dict: A dictionary with the calculated statistical measures (mean, median, std_dev).
        """
        try:

            # Calculate statistical measures
            analysis = {
                'mean': np.mean(data, axis=0),
                'median': np.median(data, axis=0),
                'std_dev': np.std(data, axis=0)
            }

            return analysis
        except Exception as e:

            return {}
