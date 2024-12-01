import os
import yaml

def get_yaml_data():
    yaml_file = os.path.join(os.path.dirname(__file__), "..\\info.yaml")
    with open (yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data