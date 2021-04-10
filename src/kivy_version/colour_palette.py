from kivy.app import App
from kivy.uix.widget import Widget
from colour_converter import ColourConverter
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
class RGBToHex(Screen):
    """
        Renders the interface that is for converting RGB values into hex.
    """
    red_input = ObjectProperty(None)
    green_input = ObjectProperty(None)
    blue_input = ObjectProperty(None)
    hex_output = ObjectProperty(None)

    def convert_rgb_to_hex(self):
        red = self.red_input
        green = self.green_input
        blue = self.blue_input
        rgb_inputs = [red, green, blue]

        for rgb_input in rgb_inputs:
            if rgb_input.text.isdigit() is False:
                rgb_input.background_color = "#FF726F"
            else:
                if int(rgb_input.text) > 255 or int(rgb_input.text) < 0:
                    rgb_input.background_color = "#FF726F"
                else:
                    rgb_input.background_color = "#FFFFFF"

        hex_value = ColourConverter.convert_rgb_to_hex(
            self,
            red.text,
            green.text,
            blue.text
        )

        # Output on interface
        if hex_value == "Invalid":
            self.hex_output.color = "#FF0000"
            self.hex_output.text = hex_value
            return
        
        self.hex_output.color = "#FFFFFF"
        self.hex_output.text = f"#{hex_value}"

class HexToRGB(Screen):
    hex_input = ObjectProperty(None)
    red_output = ObjectProperty(None)
    green_output = ObjectProperty(None)
    blue_output = ObjectProperty(None)
    error_output = ObjectProperty(None)
    
    def convert_hex_to_rgb(self):
        hex_input_contents = self.hex_input.text

        if len(hex_input_contents) == 6 or len(hex_input_contents) == 3:
            self.hex_input.background_color = "#FFFFFF"
        else:
            self.hex_input.background_color = "#FF726F"

        rgb_values = ColourConverter().convert_hex_to_rgb(hex_input_contents)
        
        if rgb_values == "Invalid":
            self.error_output.color = "#FF0000"
            self.red_output.color = "#000000"
            self.green_output.color = "#000000"
            self.blue_output.color = "#000000"
        else:
            self.error_output.color = "#000000"
            self.red_output.text = f"Red: {rgb_values[0]}"
            self.red_output.color = "#FFFFFF"
            self.green_output.color = "#FFFFFF"
            self.green_output.text = f"Green: {rgb_values[1]}"
            self.blue_output.color = "#FFFFFF"
            self.blue_output.text = f"Blue: {rgb_values[2]}"


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("colourPalette.kv")
class ColourPaletteApp(App):
    """
        The entry point of the application
    """
    def build(self):
        self.title = "Chrispy Colour Palette"
        self.icon = "favicon.ico"
        return kv

if __name__ == "__main__":
    ColourPaletteApp().run()
