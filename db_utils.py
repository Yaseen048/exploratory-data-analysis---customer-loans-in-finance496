import yaml
from sqlalchemy import create_engine
import pandas as pd



class RDSDatabaseConnector:
    def __init__(self,credentials_dict):
        self.credentials_dict = credentials_dict

    def create_engine(self):    
        self.engine = create_engine(
                "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
                    self.credentials_dict["RDS_USER"],self.credentials_dict["RDS_PASSWORD"],
                    self.credentials_dict["RDS_HOST"], self.credentials_dict["RDS_PORT"],
                    self.credentials_dict["RDS_DATABASE"]
                )
        )       
        return self.engine
    
    def extractRDSdata(self):
        with self.engine.execution_options(isolation_level='AUTOCOMMIT').connect() as conn:
            loan_payments = pd.read_sql_table('loan_payments', conn)
            print(loan_payments.head(5))
        return loan_payments




def load_credentials(filename):
    with open(filename,'r') as cred_file:
        credentials_dict = yaml.safe_load(cred_file)
    print(credentials_dict)

    return credentials_dict

def save_data(data):
    data.to_csv("loan_payments.csv", index=False)

def load_data(file):
    df = pd.read_csv(file)
    df.info()
    print(df.head(5))
    return df

yaml_file = load_credentials('credentials.yaml')
data = RDSDatabaseConnector(yaml_file)
data.create_engine()
data.extractRDSdata()
save_data(data.extractRDSdata())



df = load_data('loan_payments.csv')
