from data_reader import DataReader
from data_cleaner import DataCleaner
from sales_data_analyzer import SalesDataAnalyzer
file = DataReader(filepath="sales_data.csv")

data = file.read()

clean_data = DataCleaner(data)
updated_data = clean_data.clean_data()

analyzer = SalesDataAnalyzer(updated_data)
print(analyzer.calculate_average_order_value())
print(analyzer.calculate_total_revenue())
print(analyzer.get_top_customers_by_revenue())
