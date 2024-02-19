import pandas as pd
import data_info
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
        self.df[column].fillna(self.df[column].mode()[0], inplace = True)

    def save_formatted_data(self):
        self.df.to_csv('loan_payments_no_null.csv', index=False)

        
 

class Plotter:

    def __init__(self, data):
        self.df = pd.read_csv(data)

    def null_removal_plot(self):
            
        pass


data = DataFrameTransform('loan_payments_formatted.csv')
data.null_count()
columns = ['mths_since_last_delinq','mths_since_last_record', 'next_payment_date', 'mths_since_last_major_derog']
data.drop_col(columns)
data.drop_row(['last_payment_date', 'last_credit_pull_date','collections_12_mths_ex_med'])


col_list =['int_rate', 'funded_amount']
for col in col_list:
    data.impute_value_mean(col)

data.impute_value_median('term')
data.impute_value_mode('employment_length')
data.null_count()
data.save_formatted_data()

loan_payment = data_info.DataFrameInfo('loan_payments.csv')
loan_payment_no_null = data_info.DataFrameInfo('loan_payments_no_null.csv')

loan_payment.data_info()
loan_payment_no_null.data_info()