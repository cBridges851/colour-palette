from kivy.app import App
from kivy.uix.label import Label

class ColourPaletteApp(App):
    def build(self):
        self.title = "Chrispy Colour Palette"
        return Label(text="Hello World")

if __name__ == "__main__":
    ColourPaletteApp().run()