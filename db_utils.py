import yaml
from sqlalchemy import create_engine
import pandas as pd


class RDSDatabaseConnector:
    def __init__(self,credentials_dict):
        self.credentials_dict = credentials_dict

    def RDSDatabaseConnector(self):    

        pass
    pass



def load_credentials(filename):
    with open(filename,'r') as cred_file:
        credentials_dict = yaml.safe_load(cred_file)
    print(credentials_dict)

    return credentials_dict

load_credentials('credentials.yaml')
