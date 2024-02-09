import yaml


class RDSDatabaseConnector:
    pass

def load_credentials(filename):
    with open(filename,'r') as cred_file:
        credentials_dict = yaml.safe_load(cred_file)
    print(credentials_dict)

    return credentials_dict

load_credentials('credentials.yaml')
