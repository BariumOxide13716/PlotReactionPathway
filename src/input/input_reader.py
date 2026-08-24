
"""
This module contains the functions to read the input file
and extract the necessary information for plotting the reaction pathway.
The input file is expected to be in a specific format that defines
the style of the plot, including line colors, widths, lengths, separation, and other parameters.
The input file should also provide the data file for this code to read.

"""
from figure_details.figure_styles import key_with_str_list, \
                                         key_with_positive_float_values, \
                                         key_with_bool_values, \
                                         key_with_str_values
import os

def input_reader(input_file_path):
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
    return input_data_processor(input_data)

def input_data_processor(input_data):
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
        if key in key_with_str_list:
            processed_data[key] = [color.strip() for color in value.split(',')]
        elif key in key_with_positive_float_values:
            processed_data[key] = float(value)
        elif key in key_with_bool_values:
            processed_data[key] = value.lower() in ['true', '1', 'yes']
        elif key in key_with_str_values:
            processed_data[key] = value
        elif key == 'input_data_file':
            assert os.path.isfile(value), f"Data file {value} does not exist."
            assert value.endswith('.csv'), f"Data file {value} must be a CSV file."
            processed_data[key] = value
        elif key == 'output_plot_file':
            processed_data[key] = value
        else:
            raise ValueError(f"Unexpected key '{key}' in input data.")
    return processed_data

