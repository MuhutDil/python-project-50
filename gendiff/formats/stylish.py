import itertools

INDENT = ' '
TYPES = {'added': "+ ",
         'deleted': "- ",
         'unchanged': "  ",
         'nested': "  "
        }


def add_prefix(content, depth, symb=''):
    '''
    Adds a prefix to the given content string
    based on the depth and symbol provided.
    '''
    depth_indent = INDENT * (depth * 4 - len(symb))
    return f"{depth_indent}{symb}{content}"


def convert_value(value):
    '''
    Convert bool value to their original representation.
    '''
    if isinstance(value, (int, str)) and not isinstance(value, bool):
        return value
    return {False: 'false', True: 'true', None: 'null'}[value]


def format(data, depth=0):
    '''
    Recursively formats a nested dictionary `data`
    and returns a string representation.

    Args:
        data: The input nested dictionary to be formatted.
        depth: The current depth of the recursion (default is 0).

    Returns:
        A string representation of the formatted nested dictionary.
    '''
    if not isinstance(data, dict):
        return f'{convert_value(data)}'
    current_indent = INDENT * 4 * depth
    current_depth = depth + 1
    lines = []
    for key, descrip in data.items():
        if not isinstance(descrip, dict):
            lines.append(f'{add_prefix(key, current_depth)}: '
                         f'{format(descrip, current_depth)}')
            continue
        value = descrip.get('value')
        type_content = descrip.get('type')
        if type_content in TYPES:
            prefix = TYPES[type_content]
            lines.append(f'{add_prefix(key, current_depth, prefix)}: '
                         f'{format(value, current_depth)}')
        elif type_content == 'changed':
            old_value = value.get('old_value')
            new_value = value.get('new_value')
            lines.append(f'{add_prefix(key, current_depth, symb="- ")}: '
                         f'{format(old_value, current_depth)}')
            lines.append(f'{add_prefix(key, current_depth, symb="+ ")}: '
                         f'{format(new_value, current_depth)}')
        else:
            lines.append(f'{add_prefix(key, current_depth)}: '
                         f'{format(descrip, current_depth)}')

    result = itertools.chain('{', lines, [current_indent + '}'])
    return '\n'.join(result)