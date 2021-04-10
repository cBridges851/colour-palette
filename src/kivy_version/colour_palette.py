from kivy.app import App
from kivy.lang import Builder
from rgb_to_hex import RGBToHex
from hex_to_rgb import HexToRGB
from window_manager import WindowManager

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
