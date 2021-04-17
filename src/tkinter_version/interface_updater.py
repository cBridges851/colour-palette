from colour_converter import ColourConverter

class InterfaceUpdater:
    def update_colour_box(self, colour_box, colours):
        colour_box.configure(
            background=colours["colour box"]
        )

    def hex_updated(self, input_boxes, colour_box, colours):
        hex_value = input_boxes["hex"].get()
        rgb_values = ColourConverter().convert_hex_to_rgb(f"#{hex_value}")

        if rgb_values != "Invalid":
            input_boxes["hex"].configure(
                background=colours["secondary"]
            )

            colours["colour box"] = f"#{hex_value}"
            self.update_colour_box(colour_box, colours)

            input_boxes["red"].delete(0, "end")
            input_boxes["red"].insert(0,rgb_values[0])
            input_boxes["green"].delete(0, "end")
            input_boxes["green"].insert(0, rgb_values[1])
            input_boxes["blue"].delete(0, "end")
            input_boxes["blue"].insert(0, rgb_values[2])
        else:
            input_boxes["hex"].configure(
                background=colours["invalid input"]
            )