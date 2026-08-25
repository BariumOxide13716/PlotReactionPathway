from input.input_reader import input_reader
from data_processor.data_reader import data_reader
from data_processor.plot_data_generator import plot_data_generator
from plot.pathway_plotter import pathway_plotter

import sys
"""
This script is the main entry point for the program. 
It reads an input file, processes the data, and generates a plot based on the extracted information.
"""

def main():

    assert len(sys.argv) == 2, "Usage: python main.py <input_file_path>"
    input_file_path = sys.argv[1]
    # Read the input file and extract the necessary information
    my_styles, texts, data_file, output_plot_file = input_reader(input_file_path)

    # Read the data file and extract species, types, and energies
    species, types, energies = data_reader(data_file)

    # Generate the plot data based on the extracted information
    line_data = plot_data_generator(energies, 
                                    types,
                                    my_styles.data_display_styles)

    line_data['species_names'] = species  # Add species names to the line_data dictionary

    # Plot the data using the extracted styles and save the figure
    pathway_plotter(line_data,
                    output_plot_file, 
                    my_styles.figure_styles, 
                    my_styles.line_styles, 
                    my_styles.text_styles, 
                    texts,
                    my_styles.data_display_styles)
    

if __name__ == "__main__":
    main()