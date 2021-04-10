from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from colour_converter import ColourConverter
from colour_converter_variables import ColourConverterVariables

class RGBToHex(Screen):
    """
        Renders the interface that is for converting RGB values into hex.
    """
    red_input = ObjectProperty(None)
    green_input = ObjectProperty(None)
    blue_input = ObjectProperty(None)
    hex_output = ObjectProperty(None)

    def convert_rgb_to_hex(self):
        """
            This is the method connects the interface to the converter class.
            It displays the results of the red, blue and green input being converted 
            into hex.
        """
        red = self.red_input
        green = self.green_input
        blue = self.blue_input
        rgb_inputs = [red, green, blue]

        for rgb_input in rgb_inputs:
            if rgb_input.text.isdigit() is False:
                rgb_input.background_color = ColourConverterVariables().error_colour
            else:
                if int(rgb_input.text) > 255 or int(rgb_input.text) < 0:
                    rgb_input.background_color = ColourConverterVariables().error_colour
                else:
                    rgb_input.background_color = ColourConverterVariables().default_output_colour

        hex_value = ColourConverter.convert_rgb_to_hex(
            self,
            red.text,
            green.text,
            blue.text
        )

        if hex_value == "Invalid":
            self.hex_output.color = ColourConverterVariables().danger_colour
            self.hex_output.text = hex_value
            return
        
        self.hex_output.color = ColourConverterVariables().default_output_colour
        self.hex_output.text = f"#{hex_value}"