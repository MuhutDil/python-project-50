import pytest
import os
from gendiff import generate_diff


def build_full_path(file_name):
    return os.path.join('tests', 'fixtures', file_name)


def read_file(file_name):
    with open(build_full_path(file_name)) as file:
        output = file.read()
    return output


json_flat1 = build_full_path('json_flat1.json')
json_flat2 = build_full_path('json_flat2.json')
yaml_flat1 = build_full_path('yaml_flat1.yml')
yaml_flat2 = build_full_path('yaml_flat2.yml')
json_nested1 = build_full_path('json_nested1.json')
json_nested2 = build_full_path('json_nested2.json')
yaml_nested1 = build_full_path('yaml_nested1.yml')
yaml_nested2 = build_full_path('yaml_nested2.yml')


cases = [
    (json_flat1, json_flat2, 'test_flat.txt', 'stylish'),
    (yaml_flat1, yaml_flat2, 'test_flat.txt', 'stylish'),
    (json_flat1, yaml_flat2, 'test_flat.txt', 'stylish'),
    (json_nested1, json_nested2, 'test_nested.txt', 'stylish'),
    (yaml_nested1, yaml_nested2, 'test_nested.txt', 'stylish'),
    (json_nested1, json_nested2, 'test_plain.txt', 'plain'),
    (json_nested1, json_nested2, 'test_json.txt', 'json'),
]


@pytest.mark.parametrize('file1, file2, result, format', cases)
def test_generate_diff(file1, file2, result, format):
    assert generate_diff(file1, file2, format) == read_file(result)
