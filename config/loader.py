import json
from typing import Dict, Tuple

def load_config(config_path: str) -> Dict:
    '''
    Load configuration data from a JSON file.

    Parameters:
    - config_path (str): The path to the JSON file.

    Returns:
    - dict: A dictionary containing configuration data.
    '''
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config


def load_db(config: Dict) -> Tuple[str, str, str, str, int]:
    '''
    Extract database information from a configuration dictionary.

    Parameters:
    - config (dict): A dictionary containing configuration data, typically loaded from a JSON file.

    Returns:
    - tuple: A tuple containing database information (dbname, user, password, host, port).
    '''
    database_info = config['database']
    dbname = database_info['dbname']
    user = database_info['user']
    password = database_info['password']
    host = database_info['host']
    port = database_info['port']
    
    return dbname, user, password, host, port
