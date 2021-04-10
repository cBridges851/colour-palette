from kivy.app import App
from kivy.uix.widget import Widget
from colour_converter import ColourConverter
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
class RGBToHex(Screen):
    """
        Renders the interface of the application
    """
    red_input = ObjectProperty(None)
    green_input = ObjectProperty(None)
    blue_input = ObjectProperty(None)
    output = ObjectProperty(None)

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
            self.output.color = "#FF0000"
            self.output.text = hex_value
            return
        
        self.output.color = "#FFFFFF"
        self.output.text = f"#{hex_value}"

class HexToRGB(Screen):
    pass

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