from colour_converter import ColourConverter

class InterfaceUpdater:
    def update_colour_box(self):
        self.colour_box.configure(
            background=self.colour_box_colour
        )