from interface_updater import InterfaceUpdater
from clipboard import Clipboard
import tkinter as tk
from PIL import Image, ImageTk
from colour_converter import ColourConverter

class Renderer():
    """
        The class that renders the user interface in the Tkinter version of the application.
    """
    def __init__(self):
        """
            Initialises all the components in the user interface.
        """
        self.root = tk.Tk()
        self.colour_box = tk.Label(self.root)

        self.hex_frame = tk.LabelFrame(self.root, text="Hex")
        self.hex_label = tk.Label(self.hex_frame, text="Hex: #")
        self.hex_input = tk.Entry(self.hex_frame)
        self.hex_input.bind("<KeyRelease>", self.hex_updated)

        self.rgb_frame = tk.LabelFrame(self.root, text="RGB")
        self.red_label = tk.Label(self.rgb_frame, text="Red:")
        self.red_input = tk.Entry(self.rgb_frame)
        self.red_input.bind("<KeyRelease>", self.rgb_updated)
        self.green_label = tk.Label(self.rgb_frame, text="Green:")
        self.green_input = tk.Entry(self.rgb_frame)
        self.green_input.bind("<KeyRelease>", self.rgb_updated)
        self.blue_label = tk.Label(self.rgb_frame, text="Blue:")
        self.blue_input = tk.Entry(self.rgb_frame)
        self.blue_input.bind("<KeyRelease>", self.rgb_updated)

        self.clipboard_image = ImageTk.PhotoImage(Image.open("./clipboard.png").resize((30,30)), Image.ANTIALIAS)
        input_boxes = {
            "red": self.red_input,
            "green": self.green_input,
            "blue": self.blue_input,
            "hex": self.hex_input
        }
        self.hex_clipboard_button = tk.Button(self.hex_frame, image=self.clipboard_image, command=lambda: Clipboard().copy_to_clipboard(self.root, input_boxes, "hex"))
        self.rgb_clipboard_button = tk.Button(self.rgb_frame, image=self.clipboard_image, command=lambda: Clipboard().copy_to_clipboard(self.root, input_boxes, "rgb"))

        self.invalid_input_background = "#FF726F"
        self.default_background_colour = "#1D1D1D"
        self.secondary_colour = "#FFFFFF"
        self.default_font_size = 14
        self.colour_box_colour = "#FF0000"

    def update():
        print("updated")

    def render_colour_box(self):
        """
            Renders the box that shows the colour
        """
        self.colour_box.configure(
            width="14", 
            height="7"
        )
        InterfaceUpdater.update_colour_box(self)
        self.colour_box.grid(row=0, column=0)

    def adjust_window(self):
        """
            Sets the properties of the window of the application.
        """
        self.root.title("Chrispy Colour Palette")
        self.root.iconbitmap("favicon.ico")
        self.root.resizable(False, False)
        self.root.configure(
            bg=self.default_background_colour, 
            padx=15, 
            pady=25,
        )

    def render_hex_frame(self):
        """
            Renders the section that is for hex value input.
        """
        self.hex_frame.configure(
            bg=self.default_background_colour, 
            fg=self.secondary_colour,
            font=self.default_font_size,
            padx=10,
            pady=4
        )
        self.hex_frame.grid(row=1, column=0)

    def render_hex_label(self):
        """
            Renders the label for the hex value input.
        """
        self.hex_label.configure(
            bg=self.default_background_colour, 
            fg=self.secondary_colour,
            font=self.default_font_size
        )
        self.hex_label.grid(row=1, column=0)

    def render_hex_input(self):
        """
            Renders the input box for hex inputs
        """
        self.hex_input.configure(
            width=8,
            font=self.default_font_size
        )
        self.hex_input.grid(row=1, column=1)

    def render_rgb_frame(self):
        """
            Renders the section that is for RGB value input.
        """
        self.rgb_frame.configure(
            bg=self.default_background_colour, 
            fg=self.secondary_colour,
            font=self.default_font_size,
            padx=10,
            pady=4
        )
        self.rgb_frame.grid(row=2, column=0)
        
    def render_rgb_colour_labels(self):
        labels = [self.red_label, self.green_label, self.blue_label]
        column_counter = 0

        for label in labels:
            label.configure(
                bg=self.default_background_colour, 
                fg=self.secondary_colour,
                font=self.default_font_size
            )
            label.grid(row=0, column=column_counter)
            column_counter += 2

    def render_rgb_colour_inputs(self):
        """
            Renders the label for the RGB value input.
        """
        colour_inputs = [
            self.red_input, 
            self.green_input, 
            self.blue_input
        ]
        column_counter = 1

        for colour_input in colour_inputs:
            colour_input.configure(
                width=4,
                font=self.default_font_size
            )
            colour_input.grid(row=0, column=column_counter)
            column_counter += 2

    def render_clipboard_button(self):
        self.hex_clipboard_button.grid(row=1, column=2, padx=10)
        self.rgb_clipboard_button.grid(row=0, column=6, padx=10)

    

    def set_initial_values(self):
        """
            Sets the values that will be in the boxes when the user first opens the application.
        """
        self.hex_input.insert(0, "FF0000")
        self.red_input.insert(0, "255")
        self.green_input.insert(0, "0")
        self.blue_input.insert(0, "0")

    def render(self):
        """
            Renders the whole application.
        """
        self.adjust_window()
        self.render_colour_box()
        
        self.render_hex_frame()
        self.render_hex_label()
        self.render_hex_input()

        self.render_rgb_frame()
        self.render_rgb_colour_labels()
        self.render_rgb_colour_inputs()

        self.render_clipboard_button()

        self.set_initial_values()
        self.root.mainloop()

    

    def display_invalid_input(self, colour_input):
        colour_input.configure(
            background=self.invalid_input_background
        )

    def hex_updated(self, event):
        hex_value = self.hex_input.get()
        rgb_values = ColourConverter().convert_hex_to_rgb(f"#{hex_value}")
        if rgb_values != "Invalid":
            self.hex_input.configure(
                background=self.secondary_colour
            )

            self.colour_box_colour = f"#{hex_value}"
            InterfaceUpdater.update_colour_box(self)

            self.red_input.delete(0, "end")
            self.red_input.insert(0,rgb_values[0])
            self.green_input.delete(0, "end")
            self.green_input.insert(0, rgb_values[1])
            self.blue_input.delete(0, "end")
            self.blue_input.insert(0, rgb_values[2])
        else:
            self.hex_input.configure(
                background=self.invalid_input_background
            )
        

    def rgb_updated(self, event):
        red = self.red_input.get()
        green = self.green_input.get()
        blue = self.blue_input.get()

        colour_inputs = [
            self.red_input, 
            self.green_input,
            self.blue_input
        ]

        valid_input = True

        for colour_input in colour_inputs:
            current_colour_value = colour_input.get()

            if (current_colour_value.isdigit() is False) or (int(current_colour_value) > 255):
                self.display_invalid_input(colour_input)
                valid_input = False
            else:
                colour_input.configure(
                    background=self.secondary_colour
                )

        if valid_input is True:
            hex_value = ColourConverter().convert_rgb_to_hex(red, green, blue)
            self.colour_box_colour = f"#{hex_value}"
            InterfaceUpdater.update_colour_box(self)
            self.hex_input.delete(0, "end")
            self.hex_input.insert(0, hex_value)

Renderer().render()