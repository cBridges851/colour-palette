from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from colour_converter import ColourConverter
from colour_converter_variables import ColourConverterVariables

class HexToRGB(Screen):
    """
        Renders the interface that is for converting RGB values into hex.
    """
    hex_input = ObjectProperty(None)
    red_output = ObjectProperty(None)
    green_output = ObjectProperty(None)
    blue_output = ObjectProperty(None)
    error_output = ObjectProperty(None)
    
    def convert_hex_to_rgb(self):
        """
            This is the method connects the interface to the converter class.
            It displays the results of the hex input being converted 
            into the corresponding red, green and blue values.
        """
        hex_input_contents = self.hex_input.text

        if len(hex_input_contents) == 6 or len(hex_input_contents) == 3:
            self.hex_input.background_color = ColourConverterVariables().default_output_colour
        else:
            self.hex_input.background_color = ColourConverterVariables().error_colour

        rgb_values = ColourConverter().convert_hex_to_rgb(hex_input_contents)
        
        if rgb_values == "Invalid":
            self.error_output.color = ColourConverterVariables().danger_colour
            self.red_output.color = ColourConverterVariables().background_colour
            self.green_output.color = ColourConverterVariables().background_colour
            self.blue_output.color = ColourConverterVariables().background_colour
        else:
            self.error_output.color = ColourConverterVariables().background_colour
            self.red_output.text = f"Red: {rgb_values[0]}"
            self.red_output.color = ColourConverterVariables().default_output_colour
            self.green_output.color = ColourConverterVariables().default_output_colour
            self.green_output.text = f"Green: {rgb_values[1]}"
            self.blue_output.color = ColourConverterVariables().default_output_colour
            self.blue_output.text = f"Blue: {rgb_values[2]}"