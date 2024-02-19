import pandas as pd


class DataFrameTransform:
    
    def __init__(self, data):
        self.df = pd.read_csv(data)

    def null_count(self):
        print("Percenatge of missing values in each column:")
        print(self.df.isnull().sum()/len(self.df) *100)

    def drop_col(self, columns):
        self.df.drop(columns, axis=1, inplace=True)

    def drop_row(self, columns):
        self.df.dropna(subset= columns, inplace=True)

    def impute_value_mean(self, column):
        self.df[column].fillna(self.df[column].mean(), inplace = True)

    def impute_value_median(self, column):
        self.df[column].fillna(self.df[column].median(), inplace = True)

    def impute_value_mode(self, column):
        self.df[column].fillna(self.df[column].mode(), inplace = True)
        
 

class Plotter:
    pass

data = DataFrameTransform('loan_payments_formatted.csv')
data.null_count()
columns = ['mths_since_last_delinq','mths_since_last_record', 'next_payment_date', 'mths_since_last_major_derog']
data.drop_col(columns)
data.null_count()
data.drop_row(['last_payment_date', 'last_credit_pull_date','collections_12_mths_ex_med'])
data.null_count()
data.impute_value_mean(['int_rate', 'funded_amount'])
data.impute_value_median('term')
data.impute_value_mode('employment_length')
data.null_count()