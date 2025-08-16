def to_str(value):
    '''
    Function to convert a value to a different representation.
    '''
    scecific_values = {False: 'false', True: 'true', None: 'null'}
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, int) and not isinstance(value, bool):
        return value
    return scecific_values[value]


def describe_change(value, change_type):
    '''
    Return a string based on the given type and value.
    '''
    if change_type == 'added':
        return f'added with value: {to_str(value)}'
    elif change_type == 'deleted':
        return 'removed'
    elif change_type == 'changed':
        old_value = value.get('old_value')
        new_value = value.get('new_value')
        return (f'updated. From {to_str(old_value)}'
                + f' to {to_str(new_value)}')
    raise ValueError('Invalid type.')


def format(data, parent=''):
    '''
    Format the given difference and return a string
    representation of its properties.

    Args:
        diff: A dictionary representing the input differences.
        parent: A string representing of the full path to the root
                (default is an empty string).

    Returns:
        A string representation of the formatted differences.
    '''
    TYPES = ('added', 'deleted', 'changed')
    lines = []
    for name, descrip in data.items():
        type_content = descrip.get('type')
        value = descrip.get('value')
        full_name = f'{parent}{name}'
        if type_content in TYPES:
            lines.append(
                f"Property '{full_name}' was "
                f"{describe_change(value, type_content)}"
            )
        elif type_content == 'unchanged':
            continue
        elif type_content == 'nested':
            nested_lines = format(value, f'{full_name}.')
            lines.append(nested_lines)
    return '\n'.join(lines)
