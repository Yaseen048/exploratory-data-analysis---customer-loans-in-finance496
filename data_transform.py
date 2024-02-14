import pandas as pd

class DataTranfrom():

    def __init__(self, data):
        self.data = pd.read_csv(data)
        
    def convert_to_str(self, column):
        self.data.astype({column : 'str'})
        self.data.info()

    def convert_to_datetime():
        pass