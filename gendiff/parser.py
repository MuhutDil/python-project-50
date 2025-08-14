import json

import yaml

PARSERS = {
    'json': json.loads,
    'yml': yaml.safe_load,
    'yaml': yaml.safe_load,
}


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


def parse_data(data, format_file):
    '''
    Convert string data to a Python object based on the file format.
    '''
    parser = PARSERS.get(format_file)
    if parser is None:
        raise ValueError('Invalid file format.')
    return parser(data)


def parse_file(file_name, format_file=False):
    '''
    Converts a file to a Python object based on the file format.
    '''
    if format_file is False:
        format_file = file_name.split('.')[-1]
    file_data = read_file(file_name)
    return parse_data(file_data, format_file)