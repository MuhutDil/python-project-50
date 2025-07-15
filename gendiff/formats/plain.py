def rename_value(value):
    '''
    Function to rename a value to a different representation.
    '''
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, (int)) and not isinstance(value, bool):
        return value
    elif isinstance(value, (str)) and not isinstance(value, bool):
        return f"'{value}'"
    correct_view = {False: 'false', True: 'true', None: 'null'}
    return correct_view[value]


def differents(value, type_content):
    '''
    Return a string based on the given type and value.
    '''
    if type_content == 'added':
        return f'added with value: {rename_value(value)}'
    elif type_content == 'deleted':
        return 'removed'
    elif type_content == 'changed':
        old_value = value.get('old_value')
        new_value = value.get('new_value')
        return (f'updated. From {rename_value(old_value)}'
                + f' to {rename_value(new_value)}')
    raise ValueError('Invalid type.')


def properties(diff, parent=''):
    '''
    Generate a list of properties and their differences.

    Args:
        diff: A dictionary representing the input differences.
        parent: A string representing of the full path to the root
                (default is an empty string).

    Returns:
        A list of tuples containing the property name and its differences.
    '''
    TYPES = ('added', 'deleted', 'changed')
    lines = []
    for name, descrip in diff.items():
        type_content = descrip.get('type')
        value = descrip.get('value')
        name = f'{parent}{name}'
        if type_content in TYPES:
            lines.append((name, differents(value, type_content)))
        elif type_content == 'unchanged':
            continue
        elif type_content == 'nested':
            lines.extend((properties(value, name + '.')))
    return lines


def format(diff):
    '''
    Format the given difference and return
    a string representation of its properties.
    '''
    property_data = properties(diff)
    result = []
    for name, feature in property_data:
        result.append(f"Property '{name}' was {feature}")
    return '\n'.join(result)
