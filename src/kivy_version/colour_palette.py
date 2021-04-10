from kivy.app import App
from kivy.uix.widget import Widget
from colour_converter import ColourConverter
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
class Interface(Screen):
    """
        Renders the interface of the application
    """
    red_input = ObjectProperty(None)
    green_input = ObjectProperty(None)
    blue_input = ObjectProperty(None)
    output = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        # with self.canvas:
        #     Color(1, 0, 0, 1, mode="rgba")
        #     self.colour_display = Rectangle(pos_hint=(0, 1), size=(200,200))

    def convert_rgb_to_hex(self):
        red = self.red_input
        green = self.green_input
        blue = self.blue_input
        rgb_inputs = [red, green, blue]

        for rgb_input in rgb_inputs:
            if rgb_input.text.isdigit() is False:
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

class ColourPaletteApp(App):
    """
        The entry point of the application
    """
    def build(self):
        self.title = "Chrispy Colour Palette"
        self.icon = "favicon.ico"
        return Interface()

if __name__ == "__main__":
    ColourPaletteApp().run()