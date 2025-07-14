import json

import yaml


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


def parse_file(file_name, format=False):
    '''
    Converts a file to a Python object based on the file format.
    '''
    if format is False:
        format = file_name.split('.')[-1]
    file_data = read_file(file_name)
    if format == 'json':
        return json.loads(file_data)
    elif format == 'yml' or format == 'yaml':
        return yaml.safe_load(file_data)
    else:
        raise Exception('Invalid file format.')
