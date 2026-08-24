"""
This is a class for the parameters of styles in the plot for reaction pathways.
"""

key_with_positive_float_values = ['line_widths', 
                                  'lm_line_length',
                                  'ts_line_length',
                                  'line_separation',
                                  'plot_height', 
                                  'plot_width', 
                                  'general_text_size', 
                                  'title_text_size', 
                                  'axis_text_size', 
                                  'species_text_size', 
                                  'species_tilt_angle']
key_with_str_list = ['line_colors']
key_with_str_values = ['text_font',
                       'ordinate_label',
                       'abscissa_label',
                       'title']
key_with_bool_values = ['show_borders']

class Styles:
    def __init__(self,
                 line_colors: list[str]=None,
                 line_widths: float=1.0,
                 lm_line_length: float=1.0,
                 ts_line_length: float=1.0,
                 line_separation: float=1.0,
                 show_borders: bool=True,
                 plot_height: float=6.0,
                 plot_width: float=8.0,
                 plot_range: tuple[float, float]=None,
                 interval: float=1.0,
                 general_text_size: float=10.0,
                 title_text_size: float=12.0,
                 axis_text_size: float=10.0,
                 species_text_size: float=10.0,
                 text_font: str='Times New Roman',
                 species_tilt_angle: float=0.0,
                 ordinate_label: str='Reaction Energy (eV)',
                 abscissa_label: str='Reaction Coordinate',
                 title: str='Reaction Pathway'
                 ):

        self.line_colors = line_colors if line_colors is not None else ['blue', 'green', 'red']
        self.line_widths = line_widths
        self.lm_line_length = lm_line_length
        self.ts_line_length = ts_line_length
        self.line_separation = line_separation
        self.show_borders = show_borders
        self.plot_height = plot_height
        self.plot_width = plot_width
        self.general_text_size = general_text_size
        self.title_text_size = title_text_size
        self.axis_text_size = axis_text_size
        self.plot_range = plot_range
        self.interval = interval
        self.text_font = text_font
        self.species_text_size = species_text_size
        self.species_tilt_angle = species_tilt_angle
        self.ordinate_label = ordinate_label
        self.abscissa_label = abscissa_label
        self.title = title

    def __repr__(self):
        return (f"Styles(line_colors={self.line_colors}, "
                f"line_widths={self.line_widths}, "
                f"lm_line_length={self.lm_line_length}, "
                f"ts_line_length={self.ts_line_length}, "
                f"line_separation={self.line_separation}, "
                f"show_borders={self.show_borders}, "
                f"plot_height={self.plot_height}, "
                f"plot_width={self.plot_width}, "
                f"general_text_size={self.general_text_size}, "
                f"title_text_size={self.title_text_size}, "
                f"axis_text_size={self.axis_text_size}, "
                f"plot_range={self.plot_range}, "
                f"interval={self.interval}, "
                f"text_font='{self.text_font}', "
                f"species_text_size={self.species_text_size}, "
                f"species_tilt_angle={self.species_tilt_angle}, "
                f"ordinate_label='{self.ordinate_label}', "
                f"abscissa_label='{self.abscissa_label}', "
                f"title='{self.title}')")

    def __setattr__(self, name, value):
        """
        Usage:
        ------
        This method is used to set the attributes of the Styles class. It also validates the input
        values for each attribute to ensure they meet the expected types and constraints.
        """
        if name in key_with_str_list:
            if not isinstance(value, list) or not all(isinstance(color, str) for color in value):
                raise ValueError(f"{name} must be a list of strings.")
        elif name in key_with_positive_float_values:
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"{name} must be a positive float.")
        elif name in key_with_bool_values:
            if not isinstance(value, bool):
                raise ValueError(f"{name} must be a boolean.")
        elif name in key_with_str_values:
            if not isinstance(value, str):
                raise ValueError(f"{name} must be a string.")
        else:
            raise AttributeError(f"Unknown attribute: {name}")

        super().__setattr__(name, value)


