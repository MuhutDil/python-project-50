import pytest
import os
from gendiff import generate_diff


path_fixtures = os.path.join('tests', 'fixtures')


def read_file(path):
    with open(os.path.join(path_fixtures, path)) as file:
        output = file.read()
    return output


json_flat1 = os.path.join(path_fixtures, 'json_flat1.json')
json_flat2 = os.path.join(path_fixtures, 'json_flat2.json')
yaml_flat1 = os.path.join(path_fixtures, 'yaml_flat1.yml')
yaml_flat2 = os.path.join(path_fixtures, 'yaml_flat2.yml')
json_nested1 = os.path.join(path_fixtures, 'json_nested1.json')
json_nested2 = os.path.join(path_fixtures, 'json_nested2.json')
yaml_nested1 = os.path.join(path_fixtures, 'yaml_nested1.yml')
yaml_nested2 = os.path.join(path_fixtures, 'yaml_nested2.yml')


cases = [
    (json_flat1, json_flat2, 'test_flat.txt', 'stylish'),
    (yaml_flat1, yaml_flat2, 'test_flat.txt', 'stylish'),
    (json_flat1, yaml_flat2, 'test_flat.txt', 'stylish'),
    (json_nested1, json_nested2, 'test_nested.txt', 'stylish'),
    (yaml_nested1, yaml_nested2, 'test_nested.txt', 'stylish'),
    # (json_nested1, json_nested2, 'test_plain.txt', 'plain'),
    # (json_nested1, json_nested2, 'test_json.txt', 'json'),
]


@pytest.mark.parametrize('file1, file2, result, format', cases)
def test_generate_diff(file1, file2, result, format):
    assert generate_diff(file1, file2, format) == read_file(result)
