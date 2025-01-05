import pandas as pd


class SalesDataAnalyzer:
    """
    A class for analyzing sales data including:
        1. Total Revenue
        2. Average Order Value
        3. Top 5 Customers by Revenue
    """

    def __init__(self, data: pd.DataFrame) -> None:
        """
        Initializes the SalesDataAnalyzer with a DataFrame.

        Parameters:
            data (pd.DataFrame): The sales data.
        """

        self.data = data

    def calculate_total_revenue(self) -> float:
        """
        Calculates the total revenue.

        Returns:
            float: The total revenue.
        """

        return self.data["Revenue"].sum()

    def calculate_average_order_value(self):
        """
        Calculates the average order value.

        Returns:
            float: The average order value.
        """
        return self.data["Price"].mean()

    def get_top_customers_by_revenue(self, top_n: int = 5):
        """
        Gets the top N customers by revenue.

        Parameters:
            top_n (int): The number of top customers to return. Default is 5.

        Returns:
            pd.DataFrame: A DataFrame with the top N customers by revenue.
        """

        top_customers = self.data.groupby('Customer')['Revenue'].sum()
        return top_customers.sort_values(ascending=False).head(top_n)
