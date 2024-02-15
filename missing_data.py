import pandas as pd


class DataFrameTransform:
    
    def __init__(self, data):
        self.df = pd.read_csv(data)

    def null_count(self):
        print("Percenatge of missing values in each column:")
        print(self.df.isnull().sum()/len(self.df) *100)

    def drop_col(self, columns):
        self.df.drop(columns, axis=1, inplace=True)
        
 

class Plotter:
    pass

data = DataFrameTransform('loan_payments.csv')
data.null_count()
columns = ['mths_since_last_delinq','mths_since_last_record', 'next_payment_date', 'mths_since_last_major_derog']
data.drop_col(columns)
data.null_count()