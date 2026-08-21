"""
This is a class for the parameters of styles in the plot for reaction pathways.
The styles are about:
1. The colors of the lines
2. The width of the lines
3. The length of each line representing a reactant, an intermediate, or a product
4. The separation between the lines
5. The type for plotting a transition state, can be either a line or a curve
6. The switch to show the four borders or only the abssissa and the ordinate axes
7. The height of the plot without the title and the labels
8. The width of the plot without the title and the labels
9. The size of the titles and the labels
10. The font of the titles and the labels

"""

class Styles:
    def __init__(self,
                 line_colors: list[str]=None,
                 line_widths: float=1.0,
                 line_lengths: float=1.0,
                 line_separation: float=1.0,
                 ts_type: str='line',
                 show_borders: bool=True,
                 plot_height: float=6.0,
                 plot_width: float=8.0,
                 title_label_size: float=12.0,
                 title_label_font: str='Times New Roman',
                 ):
        """
        Parameters:
        -----------
        line_colors: list[str]
            A list of colors for the lines in the plot. If None, default colors will be used.
        line_widths: float
            The width of the lines in the plot.
        line_lengths: float
            The length of each line representing a reactant, an intermediate, or a product.
        line_separation: float
            The separation between the lines in the plot.
        ts_type: str
            The type for plotting a transition state, can be either 'line' or 'curve'.
        show_borders: bool
            The switch to show the four borders or only the abssissa and the ordinate axes.
        """
        self.line_colors = line_colors if line_colors is not None else ['blue', 'green', 'red']
        self.line_widths = line_widths
        self.line_lengths = line_lengths
        self.line_separation = line_separation
        self.ts_type = ts_type
        self.show_borders = show_borders
        self.plot_height = plot_height
        self.plot_width = plot_width
        self.title_label_size = title_label_size
        self.title_label_font = title_label_font

    def __repr__(self):
        return (f"Styles(line_colors={self.line_colors}, "
                f"line_widths={self.line_widths}, "
                f"line_lengths={self.line_lengths}, "
                f"line_separation={self.line_separation}, "
                f"ts_type='{self.ts_type}', "
                f"show_borders={self.show_borders}, "
                f"plot_height={self.plot_height}, "
                f"plot_width={self.plot_width}, "
                f"title_label_size={self.title_label_size}, "
                f"title_label_font='{self.title_label_font}')")

    def __setattr__(self, name, value):
        """
        Usage:
        ------
        This method is used to set the attributes of the Styles class. It also validates the input
        values for each attribute to ensure they meet the expected types and constraints.
        """
        if name == 'line_colors':
            if not isinstance(value, list) or not all(isinstance(color, str) for color in value):
                raise ValueError("line_colors must be a list of strings.")
        elif name == 'line_widths':
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("line_widths must be a positive number.")
        elif name == 'line_lengths':
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("line_lengths must be a positive number.")
        elif name == 'line_separation':
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("line_separation must be a positive number.")
        elif name == 'ts_type':
            if value not in ['line', 'curve']:
                raise ValueError("ts_type must be either 'line' or 'curve'.")
        elif name == 'show_borders':
            if not isinstance(value, bool):
                raise ValueError("show_borders must be a boolean.")
        elif name == 'plot_height':
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("plot_height must be a positive number.")
        elif name == 'plot_width':
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("plot_width must be a positive number.")
        elif name == 'title_label_size':
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("title_label_size must be a positive number.")
        elif name == 'title_label_font':
            if not isinstance(value, str):
                raise ValueError("title_label_font must be a string.")
        super().__setattr__(name, value)


