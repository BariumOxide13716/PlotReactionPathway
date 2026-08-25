
"""
This module contains the functions to read the input file
and extract the necessary information for plotting the reaction pathway.
The input file is expected to be in a specific format that defines
the style of the plot, including line colors, widths, lengths, separation, and other parameters.
The input file should also provide the data file for this code to read.

"""
from figure_details.figure_styles import Styles
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
    
    my_styles = Styles()  # Create an instance of the Styles class to hold the styles
    texts = {
        'ordinate_label': None,
        'abscissa_label': None,
        'title': None
    }

    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue  # Skip empty lines and comments
            key, value = line.split('=')
            key = key.strip().lower()
            if key == 'data_file':
                data_file = value.strip()
            elif key == 'output_file':
                output_file = value.strip()
            elif key in texts.keys():
                texts[key] = value.strip()  # Store the text values in the texts dictionary
            else:
                my_styles.set_value(key.strip(), value.strip())  # Set the attribute in the Styles instance

    assert 'data_file' in locals(), "Data file not specified in the input file."
    assert 'output_file' in locals(), "Output plot file not specified in the input file."
    print(f"Data file specified in input: {data_file if 'data_file' in locals() else 'Not specified'}")
    my_styles.print_styles()  # Print the styles for verification
    return my_styles, texts, data_file, output_file