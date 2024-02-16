import pandas as pd
from dateutil.parser import parse

class DataTranfrom:

    def __init__(self, data):
        self.df = pd.read_csv(data)
        
    def convert_to_category(self, column):
        self.df[column] = self.df[column].astype('category')
        print(self.df[column].head(5))
        self.df.info()

    def convert_to_datetime(self, column):
        self.df[column] = self.df[column].astype('datetime64[ns]')
        self.df.info()
        print(self.df[column].head(5))

    def remove_units(self, column):
        self.df[column] = self.df[column].str.replace(r'\D', '',regex=True)
        self.df[column] = self.df[column].astype('float')
        

        



formatted_data = DataTranfrom('loan_payments.csv')
formatted_data.remove_units('term')
cat_columns = ['grade', 'sub_grade', 'home_ownership', 'verification_status', 'loan_status', 'payment_plan', 'purpose', 'application_type']
date_columns = ['issue_date', 'earliest_credit_line','last_payment_date', 'last_credit_pull_date', 'next_payment_date']
formatted_data.convert_to_category(cat_columns)
formatted_data.convert_to_datetime(date_columns)




