
"""
This module contains the functions to generate the starting and ending points
of the lines for the reaction pathway plot.

The ordinate of the starting and ending points of the lines are the energies 
of the local minima and transition states.
The abscissa of the starting and ending points of the lines are calculated 
based on the data_type, lm_line_length, ts_line_length, and line_separation.
Below is an example:

suppose the data_type is [0, 1, 0, 0, 1], l
m_line_length = 1, 
ts_line_length = 0.5,
line_separation = 0.4,
and the first entry of energies is [0.0, 1.0, 0.5, 0.2, 1.5], 
then the starting and ending points of the lines are:
    (0.4, 0.0) (1.4, 0.0)
    (1.8, 1.0) (2.3, 1.0)
    (2.7, 0.5) (3.7, 0.5)
    (4.1, 0.2) (5.1, 0.2)
    (5.5, 1.5) (6.0, 1.5)
and the starting and the ending points for the connecting lines are:
    (1.4, 0.0) (1.8, 1.0)
    (2.3, 1.0) (2.7, 0.5)
    (3.7, 0.5) (4.1, 0.2)
    (5.1, 0.2) (5.5, 1.5)

Suppose the second entry of energies is [0.1, 1.1, None, 0.3, 1.6],
then the starting and ending points of the lines are:
    (0.4, 0.1) (1.4, 0.1)
    (1.8, 1.1) (2.3, 1.1)
    (4.1, 0.3) (5.1, 0.3)
    (5.5, 1.6) (6.0, 1.6)
and the connecting lines are:
    (1.4, 0.1) (1.8, 1.1)
    (2.3, 1.1) (4.1, 0.3)
    (5.1, 0.3) (5.5, 1.6)
"""


def plot_data_generator(energy_lists: list[list[float|None]],
                        data_type: list[int],
                        lm_line_length: float = 1.0,
                        ts_line_length: float = 1.0,
                        line_separation: float = 0.5):

    abscissa_starting_points, abscissa_ending_points = abscissa_generator(data_type,
                                                                         lm_line_length,
                                                                         ts_line_length,
                                                                         line_separation)

    line_coordiante_list = line_coordiante_generator(energy_lists,
                                                     abscissa_starting_points,
                                                     abscissa_ending_points)
    connecting_line_coordinate_list = connecting_line_coordinate_generator(line_coordiante_list)

    return line_coordiante_list, \
           connecting_line_coordinate_list, \
           abscissa_starting_points, \
           abscissa_ending_points

def connecting_line_coordinate_generator(line_coordinate_list: list[list[tuple[tuple[float, float], tuple[float, float]]]]):
    connecting_line_coordinate_list = []
    for line_coordinates in line_coordinate_list:
        connecting_line_coordinates = []
        for i in range(len(line_coordinates) - 1):
            connecting_line_coordinates.append((line_coordinates[i][1], line_coordinates[i + 1][0]))
        connecting_line_coordinate_list.append(connecting_line_coordinates)

    return connecting_line_coordinate_list

def line_coordiante_generator(energy_lists: list[list[float|None]],
                              abscissa_starting_points: list[float],
                              abscissa_ending_points: list[float]):
    line_coordinate_list = []
    for energy_list in energy_lists:
        line_coordinates = []
        for i, energy in enumerate(energy_list):
            if energy is not None:
                line_coordinates.append(((abscissa_starting_points[i], energy),
                                         (abscissa_ending_points[i], energy)))
        line_coordinate_list.append(line_coordinates)

    return line_coordinate_list

def abscissa_generator(data_type: list[int],
                       lm_line_length: float = 1.0,
                       ts_line_length: float = 1.0,
                       line_separation: float = 0.5):
    abscissa_starting_points = []
    abscissa_ending_points = []

    current_starting_point = line_separation
    for i, t in enumerate(data_type):
        abscissa_starting_points.append(current_starting_point)
        if t == 0:
            abscissa_ending_points.append(current_starting_point + lm_line_length)
            current_starting_point += lm_line_length + line_separation
        elif t == 1:
            abscissa_ending_points.append(current_starting_point + ts_line_length)
            current_starting_point += ts_line_length + line_separation

    return abscissa_starting_points, abscissa_ending_points

