"""
This module contains the function to read the data for reaction energies.

The csv file is expected to have the following information
the spaces are just for better visualization, the actual csv file should not have any spaces.

species1, species2, species3, species4, species5, ...
0,        1,        0,        0,        1, ...
energy11, energy12, energy13, energy14, energy15, ...
energy21, energy22, energy23, energy24, energy25, ...
...

the species row is the first row.
The second row shows whether a species is a local minimum (0) or a transition state (1).

energy11, energy12, energy13, energy14, energy15, ... are the energies of the first reaction.
energy21, energy22, energy23, energy24, energy25, ... are the energies of the second reaction.
and so on and so forth.
Usually these reactions mean the same reaction but on different surfaces, or with different methods, 
or with different parameters. 
Some of these energies can be empty, which means that the corresponding species is not present in that reaction.

The speciess are stored in a list of strings,
the local minimum and transition state information is stored in a list of integers,
and the energies are stored in a list of lists of floats.

"""
import csv

def data_reader(file_path: str):
    species = []
    types = []
    energies = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        species = next(reader)
        types = list(map(int, next(reader)))
        for row in reader:
            energy_row = []
            for item in row:
                if item == '':
                    energy_row.append(None)
                else:
                    energy_row.append(float(item))
            energies.append(energy_row)

    return species, types, energies