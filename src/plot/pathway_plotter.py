"""
This module generates the figures based on the following data:
    line_coordiantes,
    connecting_line_coordinates,
    species_names,
    abscissa_starting_points,
    species_name_tilt_angle

the following styles for the figure:
    show_all_borders: whether to show all four boarders, or only the left and bottom boarders
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

#   ---- Plot Styles ----
    # starting by creating the figure and axes
    fig, ax = plt.subplots(figsize=(figure_styles['plot_dimension'][0], figure_styles['plot_dimension'][1]))
    # to set the range of the figure in the ordinate direction
    ax.set_ylim(figure_styles['plot_range'][0], figure_styles['plot_range'][1])
    # set the interval of the ticks in the ordinate direction to the nearest integer of the interval specified in the figure_styles
    ax.yaxis.set_ticks([i for i in range(int(figure_styles['plot_range'][0]), int(figure_styles['plot_range'][1]) + 1, int(figure_styles['interval']))])
    # set the figure to show only the left and bottom boarders if show_boarders is set to False
    if not figure_styles['show_all_borders']:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    # set the abscissa values as invisible
    ax.xaxis.set_visible(False)

#   ---- Text Styles ----
    # set the texts as taht in text_styles['text_font'] and text_styles['general_text_size']
    plt.rcParams['font.family'] = text_styles['text_font']
    plt.rcParams['font.size'] = text_styles['general_text_size']

#   ---- Texts ----
    # set the ordinate label, abscissa label, and title as specified in texts
    if texts['ordinate_label'] is not None:
        ax.set_ylabel(texts['ordinate_label'], fontsize=text_styles['axis_text_size'])
    if texts['abscissa_label'] is not None:
        ax.set_xlabel(texts['abscissa_label'], fontsize=text_styles['axis_text_size'], labelpad=text_styles['abscissa_label_ordinate'])
    if texts['title'] is not None:
        ax.set_title(texts['title'], fontsize=text_styles['title_text_size'])


#   ---- Reaction Pathway Plotting ----
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
            print(f"Plotting line segment: {line_segment} with color: {line_styles['color'][i]} and width: {line_styles['width']}")
            x_to_plot = [ line_segment[0][0], line_segment[1][0] ]
            y_to_plot = [ line_segment[0][1], line_segment[1][1] ]
            ax.plot(x_to_plot, y_to_plot, color=line_styles['color'][i], linewidth=line_styles['width'])

    #then plot the dash lines for the connecting lines
    for i, connecting_lines in enumerate(line_data['connecting_coordinates']):
        for line_segment in connecting_lines:
            x_to_plot = [ line_segment[0][0], line_segment[1][0] ]
            y_to_plot = [ line_segment[0][1], line_segment[1][1] ]
            ax.plot(x_to_plot, y_to_plot, color=line_styles['color'][i], linewidth=line_styles['width'], linestyle='dashed')

#   ---- Species Names Plotting ----
    #next, loop over each string in line_data['species_names'] and plot the species
    #names, each string starts from the abscissa_starting_points as the abscissa value, 
    #at species_text_ordinate below the abscissa, and is tilted by species_name_tilt_angle
    for i, species_names in enumerate(line_data['species_names']):
        ax.text(line_data['abscissa_starting_points'][i],
                text_styles['species_text_ordinate'] + figure_styles['plot_range'][0],
                species_names,
                fontsize=text_styles['species_text_size'],
                rotation=data_display_styles['species_tilt_angle'],
                ha='left',
                va='top')

    #now we save the figure to the output_plot_file
    plt.savefig(output_plot_file, bbox_inches='tight', dpi=300)

    

    

    