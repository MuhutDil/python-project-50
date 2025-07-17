### Hexlet tests and linter status:
[![Actions Status](https://github.com/MuhutDil/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MuhutDil/python-project-50/actions)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=MuhutDil_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=MuhutDil_python-project-50)

# Gendiff

This CLI application 'gendiff' is able to compare 2 json or yaml files.
On the command line you need to specify two files and an optional output format. \
Output formats: 
- stylish (default)
- plain
- json

## Installation
### Prerequisites
- Python version 3.10 or higher
- PyYaml version 6.0.2 or higher
- Uv version 0.5 or higher (optional)

### Download
    uv tool install https://github.com/MuhutDil/python-project-50.git
or

    git clone https://github.com/MuhutDil/python-project-50.git
 
#### Start commands
```gendiff [-h] [-f FORMAT] <first_file> <second_file>```

### Below are examples of work.
#### Comparison of two flat json files (stylish)
[![asciicast](https://asciinema.org/a/728071.svg)](https://asciinema.org/a/728071)
#### Comparison of two flat yaml files (stylish)
[![asciicast](https://asciinema.org/a/728072.svg)](https://asciinema.org/a/728072)
#### Comparison of two nested files (stylish)
[![asciicast](https://asciinema.org/a/728073.svg)](https://asciinema.org/a/728073)
#### Comparison of two files in plain format
[![asciicast](https://asciinema.org/a/728074.svg)](https://asciinema.org/a/728074)
#### Comparison of two files in json format
[![asciicast](https://asciinema.org/a/728076.svg)](https://asciinema.org/a/728076)
