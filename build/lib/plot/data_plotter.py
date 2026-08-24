"""
This module generates the figures based on the following data:
    line_coordiantes,
    connecting_line_coordinates,
    species_names,
    abscissa_starting_points,
    species_name_tilt_angle

the following styles for the figure:
    show_borders: whether to show all four boarders, or only the left and bottom boarders
    plot_height and plot_width: the height and width of the figure
    plot_range: the range of the figure in the ordinate directions
    interval: the interval of the ticks in the ordinate direction

the following styles for the lines:
    line_color: the color of the lines
    line_width: the width of the lines

the following styles for texts:
    text_font: the font of the texts
    general_text_size: the size of the general texts
    title_text_size: the size of the title text
    axis_text_size: the size of the axis texts
    species_text_size: the size of the species names

the following contents:
    ordinate_label: the label of the ordinate
    abscissa_label: the label of the abscissa
    title: the title of the figure

and the place to save the figure set by output_plot_file
"""

figure_styles = {
    'show_boarders': True,
    'plot_dimension': [8, 6],  # width, height
    'plot_range': [-2, 2],  # min, max
    'interval': 0.5
}

line_styles = {
    'color': None,
    'width': 1.0
}

text_styles = {
    'font': 'Times New Roman',
    'general_text_size': 12,
    'title_text_size': 14,
    'axis_text_size': 10,
    'species_text_size': 10
}

texts = {
    'ordinate_label': "Energy (eV)",
    'abscissa_label': "Reaction Coordinate",
    'title': "Reaction Pathway"
}

data_display_styles = {
    'species_tilt_angle': 0.0
}

line_data = {
    'coordinates': None,
    'connecting_coordinates': None,
    'species_names': None,
    'abscissa_starting_points': None
}
import matplotlib.pyplot as plt
def pathway_plotter(line_data: dict,
                    output_plot_file: str,
                    figure_styles: dict,
                    line_styles: dict,
                    text_styles: dict,
                    texts: dict,
                    data_display_styles: dict
                    ):

    # first of all, adding all the styles to the figure.

    # starting by creating the figure and axes
    fig, ax = plt.subplots(figsize=(figure_styles['plot_dimension'][0], figure_styles['plot_dimension'][1]))
    # then to set the range of the figure in the ordinate direction
    ax.set_ylim(figure_styles['plot_range'][0], figure_styles['plot_range'][1])
    # then to set the interval of the ticks in the ordinate direction to the nearest integer of the interval specified in the figure_styles
    ax.yaxis.set_ticks([i for i in range(int(figure_styles['plot_range'][0]), int(figure_styles['plot_range'][1]) + 1, int(figure_styles['interval']))])
    # then set the figure to show only the left and bottom boarders if show_boarders is set to False
    if not figure_styles['show_boarders']:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    #next, loop over each entry in line_data['coordinates'] and plot the lines
    #with the line_width and line_color specified in line_styles

    # but before that, the line_color needs to be have the same length as the number of entries in line_data['coordinates']
    if line_styles['color'] is None:
        line_styles['color'] = ['black'] * len(line_data['coordinates'])
    if len(line_styles['color']) != len(line_data['coordinates']):
        # repeat the colors until it has the same length as the number of entries in line_data['coordinates']
        line_styles['color'] = (line_styles['color'] * (len(line_data['coordinates']) // len(line_styles['color']) + 1))[:len(line_data['coordinates'])]

    #within plotting the lines, first plot the energies for local minima and transition states as solid lines
    for i, coord_lines in enumerate(line_data['coordinates']):
        # if you go to the plot_data_generator, you will see that the coord_lines is a list of lists, where each list contains the coordinates of a line segment.
        for line_segment in coord_lines:
            x_to_plot = [ line_segment[0, 0], line_segment[1, 0] ]
            y_to_plot = [ line_segment[0, 1], line_segment[1, 1] ]
            ax.plot(x_to_plot, y_to_plot, color=line_styles['color'][i], linewidth=line_styles['width'])

    #then plot the dash lines for the connecting lines
    for i, connecting_lines in enumerate(line_data['connecting_coordinates']):
        for line_segment in connecting_lines:
            x_to_plot = [ line_segment[0, 0], line_segment[1, 0] ]
            y_to_plot = [ line_segment[0, 1], line_segment[1, 1] ]
            ax.plot(x_to_plot, y_to_plot, color=line_styles['color'][i], linewidth=line_styles['width'], linestyle='dashed')


    #now we save the figure to the output_plot_file
    plt.savefig(output_plot_file, bbox_inches='tight', dpi=300)

    

    

    