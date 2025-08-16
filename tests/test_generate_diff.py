import pytest
import os
from gendiff import generate_diff


def build_full_path(file_name):
    return os.path.join('tests', 'fixtures', file_name)


def read_file(file_name):
    with open(build_full_path(file_name)) as file:
        output = file.read()
    return output


cases = [
    ('json_flat1.json', 'json_flat2.json', 'test_flat.txt', 'stylish'),
    ('yaml_flat1.yml', 'yaml_flat2.yml', 'test_flat.txt', 'stylish'),
    ('json_flat1.json', 'yaml_flat2.yml', 'test_flat.txt', 'stylish'),
    ('json_nested1.json', 'json_nested2.json', 'test_nested.txt', 'stylish'),
    ('yaml_nested1.yml', 'yaml_nested2.yml', 'test_nested.txt', 'stylish'),
    ('json_nested1.json', 'json_nested2.json', 'test_plain.txt', 'plain'),
    ('json_nested1.json', 'json_nested2.json', 'test_json.txt', 'json'),
]


@pytest.mark.parametrize('file_name1, file_name2, result, format', cases)
def test_generate_diff(file_name1, file_name2, result, format):
    file1 = build_full_path(file_name1)
    file2 = build_full_path(file_name2)
    assert generate_diff(file1, file2, format) == read_file(result)
