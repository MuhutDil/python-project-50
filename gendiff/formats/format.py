from gendiff.formats.json import format as json_format
from gendiff.formats.plain import format as plain
from gendiff.formats.stylish import format as stylish

FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format,
}


def apply_selected_format(data, selected_format):
    """Applies a specified formatting style to the input data.
    
    Args:
        data: The data to be formatted.
        selected_format: A string key specifying the desired output format.
                         Must exist in the FORMATS dictionary.
    
    Returns:
        str: Formatted data. The exact return type depends on the
            selected formatter.
    
    Raises:
        ValueError: If the specified format is not found in FORMATS.
    """
    style_format = FORMATS.get(selected_format)
    if style_format is None:
        raise ValueError('Invalid format.')
    return style_format(data)