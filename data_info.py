import pandas as pd
from statistics import mean, median, stdev


class DataFrameInfo:
    def __init__(self, data):
        self.df = pd.read_csv(data)
    
    def data_info(self):
        self.df.info()

    def stat_value(self, column):
        mean_av = mean(self.df[column])
        median_av = median(self.df[column])
        standard_dev = stdev(self.df[column])
        print(f'The mean {column} is {mean_av}.\n',
              f'The median of {column} is {median_av}\n',
              f'The standard deviation of {column} is {standard_dev}')

data = DataFrameInfo('loan_payments.csv')
data.data_info()
data.stat_value('funded_amount_inv')
        