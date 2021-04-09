from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from colour_converter import ColourConverter

class Interface(Widget):
    """
        Renders the interface of the application
    """
    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        
        # with self.canvas:
        #     Color(1, 0, 0, 1, mode="rgba")
        #     self.colour_display = Rectangle(pos_hint=(0, 1), size=(200,200))

    def convert(self):
        print("example has been triggered")

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