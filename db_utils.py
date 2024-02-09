import yaml
from sqlalchemy import create_engine
import pandas as pd


class RDSDatabaseConnector:
    def __init__(self,credentials_dict):
        self.credentials_dict = credentials_dict

    def RDSDatabaseConnector(self):    
        engine = create_engine(
                url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
                    self.credentials_dict["RDS_USER"],self.credentials_dict["RDS_PASSWORD"],
                    self.credentials_dict["RDS_HOST"], self.credentials_dict["RDS_PORT"],
                    self.credentials_dict["RDS_DATABASE"]
                )
        )
        
        pass
    pass



def load_credentials(filename):
    with open(filename,'r') as cred_file:
        credentials_dict = yaml.safe_load(cred_file)
    print(credentials_dict)

    return credentials_dict

load_credentials('credentials.yaml')
