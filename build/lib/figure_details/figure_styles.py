"""
This is a class for the parameters of styles in the plot for reaction pathways.
"""

key_with_str_list = ['line_colors']
key_with_positive_float_values = [
                                  'interval',
                                  'general_text_size',
                                  'title_text_size',
                                  'axis_text_size',
                                  'species_text_size',
                                  'lm_line_length', 
                                  'ts_line_length', 
                                  'line_separation', 
                                  'species_tilt_angle',
                                  'species_text_ordinate',
                                  'abscissa_label_ordinate'
                                  ]
key_with_bool_values = ['show_all_borders']
key_with_str_values = ['text_font']
key_with_float_list_values = [ 'line_widths'
                               'plot_size', 
                               'plot_range' ]

line_style_keys = ['line_colors', 
                    'line_widths']
figure_style_keys = ['show_all_borders', 
                     'plot_size', 
                     'plot_range', 
                     'interval']
text_styles_keys = ['general_text_size', 
                    'title_text_size', 
                    'axis_text_size', 
                    'species_text_size', 
                    'text_font']
data_display_styles_keys = ['lm_length', 
                            'ts_length', 
                            'separation', 
                            'species_tilt_angle']

class Styles:
    def __init__(self,
                # --- line styles ---
                 line_colors: list[str]=['black'],
                 line_widths: list[float] = [2.0],
                # --- figure styles ---
                 show_all_borders: bool=True,
                 plot_size: list[float]=[8.0, 6.0],
                 plot_range: list[float]=[-2.0, 2.0],
                 interval: float=1.0,
                # --- text styles ---
                 general_text_size: float=10.0,
                 title_text_size: float=12.0,
                 axis_text_size: float=10.0,
                 species_text_size: float=10.0,
                 species_text_ordinate: float=-0.5, # the ordinate value for the species names
                                                    # relative to the minimum of plot range
                 abscissa_label_ordinate: float=-2.0, # the ordinate value for the abscissa label
                 text_font: str='Arial', 
                # --- data display styles ---
                 lm_line_length: float=1.0, 
                 ts_line_length: float=0.5,
                 line_separation: float=0.5,
                 species_tilt_angle: float=0.0
                 ):

        self.line_styles = {}
        self.figure_styles = {}
        self.text_styles = {}
        self.data_display_styles = {}



        self.line_styles['line_colors'] = line_colors
        self.line_styles['line_widths'] = line_widths

        self.figure_styles['show_all_borders'] = show_all_borders
        self.figure_styles['plot_size'] = plot_size
        self.figure_styles['plot_range'] = plot_range
        self.figure_styles['interval'] = interval

        self.text_styles['general_text_size'] = general_text_size
        self.text_styles['title_text_size'] = title_text_size
        self.text_styles['axis_text_size'] = axis_text_size
        self.text_styles['species_text_size'] = species_text_size
        self.text_styles['species_text_ordinate'] = species_text_ordinate
        self.text_styles['abscissa_label_ordinate'] = abscissa_label_ordinate
        self.text_styles['text_font'] = text_font

        self.data_display_styles['lm_length'] = lm_line_length
        self.data_display_styles['ts_length'] = ts_line_length
        self.data_display_styles['separation'] = line_separation
        self.data_display_styles['species_tilt_angle'] = species_tilt_angle

    def set_value(self, name, value):
        if name in key_with_bool_values:
            try:
                converted_value = bool(value)
            except ValueError:
                raise ValueError(f"Invalid value for {name}: {value}. Expected a boolean value.")
        elif name in key_with_positive_float_values:
            try:
                converted_value = float(value)
                if converted_value <= 0:
                    raise ValueError(f"Invalid value for {name}: {value}. Expected a positive float.")
            except ValueError:
                raise ValueError(f"Invalid value for {name}: {value}. Expected a positive float.")
        elif name in key_with_str_list:
            if isinstance(value, str):
                converted_value = [v.strip() for v in value.split()]
            elif isinstance(value, list):
                converted_value = [str(v).strip() for v in value]
            else:
                raise ValueError(f"Invalid value for {name}: {value}. Expected a string or a list of strings.")
        elif name in key_with_float_list_values:
            if isinstance(value, str):
                converted_value = [float(v.strip()) for v in value.split()]
            elif isinstance(value, list):
                converted_value = [float(v) for v in value]
            else:
                raise ValueError(f"Invalid value for {name}: {value}. Expected a string or a list of floats.")
        elif name in key_with_str_values:
            print(f"value before conversion: {value}")
            converted_value = value
            print(f"value after conversion: {converted_value}")
        else:
            print(f"current name: {name}")
            raise f"Invalid key: {name}"

        if name in line_style_keys:
            self.line_styles[name] = converted_value
        elif name in figure_style_keys:
            self.figure_styles[name] = converted_value
        elif name in text_styles_keys:
            self.text_styles[name] = converted_value
        elif name in data_display_styles_keys:
            self.data_display_styles[name] = converted_value
        elif name in [ 'line_styles', 'figure_styles', 'text_styles', 'data_display_styles']:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Unknown attribute: {name}")

    def print_styles(self):
        print("Line Styles:")
        for key in line_style_keys:
            print(f"  {key}: {self.line_styles.get(key)}")

        print("\nFigure Styles:")
        for key in figure_style_keys:
            print(f"  {key}: {self.figure_styles.get(key)}")

        print("\nText Styles:")
        for key in text_styles_keys:
            print(f"  {key}: {self.text_styles.get(key)}")

        print("\nData Display Styles:")
        for key in data_display_styles_keys:
            print(f"  {key}: {self.data_display_styles.get(key)}")
