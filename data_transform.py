import pandas as pd

class DataTranfrom():

    def __init__(self, data):
        self.df = pd.read_csv(data)
        
    def convert_to_str(self, column):
        self.df[column] = self.df[column].astype('string')
        self.df.info()

    def convert_to_datetime():
        pass


formatted_data = DataTranfrom('loan_payments.csv')
formatted_data.convert_to_str('grade')