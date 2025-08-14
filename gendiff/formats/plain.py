def convert_value(value):
    '''
    Function to convert a value to a different representation.
    '''
    scecific_values = {False: 'false', True: 'true', None: 'null'}
    if isinstance(value, dict):
        return '[complex value]'
    elif value in scecific_values:
        return scecific_values[value]
    elif isinstance(value, str):
        return f"'{value}'"
    return value


def describe_change(value, change_type):
    '''
    Return a string based on the given type and value.
    '''
    if change_type == 'added':
        return f'added with value: {convert_value(value)}'
    elif change_type == 'deleted':
        return 'removed'
    elif change_type == 'changed':
        old_value = value.get('old_value')
        new_value = value.get('new_value')
        return (f'updated. From {convert_value(old_value)}'
                + f' to {convert_value(new_value)}')
    raise ValueError('Invalid type.')


def generate_diff_report(data, parent=''):
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
    for name, descrip in data.items():
        type_content = descrip.get('type')
        value = descrip.get('value')
        name = f'{parent}{name}'
        if type_content in TYPES:
            lines.append((name, describe_change(value, type_content)))
        elif type_content == 'unchanged':
            continue
        elif type_content == 'nested':
            lines.extend((generate_diff_report(value, name + '.')))
    return lines


def format(data):
    '''
    Format the given difference and return
    a string representation of its properties.
    '''
    diff = generate_diff_report(data)
    return '\n'.join(
        f"Property '{name}' was {feature}"
        for name, feature in diff
    )
