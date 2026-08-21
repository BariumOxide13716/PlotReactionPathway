
"""
This module contains the functions to read the input file
and extract the necessary information for plotting the reaction pathway.
The input file is expected to be in a specific format that defines
the style of the plot, including line colors, widths, lengths, separation, and other parameters.
The input file should also provide the data file for this code to read.

"""
import os
def read_input_file(input_file_path):
    """
    Reads the input file and extracts the necessary information for plotting the reaction pathway.

    Parameters:
    -----------
    input_file_path : str
        The path to the input file.
    Returns:
    --------
    dict
        A dictionary containing the extracted information from the input file.
    Raises:
    -------
    ValueError
        If the input file is not in the expected format or if required information is missing.
    """

    assert os.path.isfile(input_file_path), f"Input file {input_file_path} does not exist."
    input_data = {}
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue  # Skip empty lines and comments
            key, value = line.split('=')
            input_data[key.strip()] = value.strip()
    return process_input_data(input_data)

def process_input_data(input_data):
    """
    Processes the extracted input data and converts it into the appropriate types.

    Parameters:
    -----------
    input_data : dict
        A dictionary containing the extracted information from the input file.
    Returns:
    --------
    dict
        A dictionary containing the processed information with appropriate types.
    Raises:
    -------
    ValueError
        If any of the values cannot be converted to the expected type.
    """
    processed_data = {}
    for key, value in input_data.items():
        if key == 'line_colors':
            processed_data[key] = [color.strip() for color in value.split(',')]
        elif key in ['line_widths', 'line_lengths', 'line_separation', 'plot_height', 'plot_width', 'title_label_size']:
            processed_data[key] = float(value)
        elif key == 'ts_type':
            if value not in ['line', 'curve']:
                raise ValueError("ts_type must be either 'line' or 'curve'.")
            processed_data[key] = value
        elif key == 'show_borders':
            processed_data[key] = value.lower() in ['true', '1', 'yes']
        elif key == 'title_label_font':
            processed_data[key] = value
        else:
            raise ValueError(f"Unexpected key '{key}' in input data.")
    return processed_data

