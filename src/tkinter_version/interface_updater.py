from colour_converter import ColourConverter

class InterfaceUpdater:
    """
        The class that is responsible for updating the UI
    """
    def update_colour_box(self, colour_box, colours):
        """
            The method that updates the box which displays the inputted colour
            Args:
                colour_box: Label, the box which displays the colour inputted
                colours: object, the main colours used in the application
        """
        colour_box.configure(
            background=colours["colour box"]
        )

    def display_invalid_input(self, colour_input, colours):
        """
            The method responsible for indicating when there has been an invalid
            input.
            Args:
                colour_input: Entry, the input box where the user has inputted an invalid value into
                colours: object, the main colours for the application
        """
        colour_input.configure(
            background=colours["invalid input"]
        )

    def hex_updated(self, input_boxes, colour_box, colours):
        """
            The method that is called when the hex input box has been inputted to, meaning the 
            RGB boxes are changed.
            Args:
                input_boxes: list, contains all the input boxes in the application
                colour_box: Label, the box which displays the colour inputted
                colours: object, the main colours for the application
        """
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
            self.display_invalid_input(input_boxes["hex"], colours)

    def rgb_updated(self, input_boxes, colour_box, colours):
        """
            The method that is called when an RGB input box has been inputted to, meaning the 
            hex box is changed.
            Args:
                input_boxes: list, contains all the input boxes in the application
                colour_box: Label, the box which displays the colour inputted
                colours: object, the main colours for the application
        """
        red = input_boxes["red"].get()
        green = input_boxes["green"].get()
        blue = input_boxes["blue"].get()

        colour_inputs = [
            input_boxes["red"], 
            input_boxes["green"],
            input_boxes["blue"]
        ]

        valid_input = True

        for colour_input in colour_inputs:
            current_colour_value = colour_input.get()

            if (current_colour_value.isdigit() is False) or (int(current_colour_value) > 255):
                self.display_invalid_input(colour_input, colours)
                valid_input = False
            else:
                colour_input.configure(
                    background=colours["secondary"]
                )

        if valid_input is True:
            hex_value = ColourConverter().convert_rgb_to_hex(red, green, blue)
            colours["colour box"] = f"#{hex_value}"
            InterfaceUpdater.update_colour_box(self, colour_box, colours)
            input_boxes["hex"].delete(0, "end")
            input_boxes["hex"].insert(0, hex_value)
