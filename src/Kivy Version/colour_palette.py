from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color

class Interface(Widget):
    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        
        with self.canvas:
            Color(1, 0, 0, 1, mode="rgba")
            self.colour_display = Rectangle(pos=(300, 360), size=(200,200))


class ColourPaletteApp(App):
    def build(self):
        self.title = "Chrispy Colour Palette"
        return Interface()

if __name__ == "__main__":
    ColourPaletteApp().run()