import tkinter as tk
from tkinter.constants import SOLID
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

    def render_colour_box(self):
        """
            Renders the box that shows the colour
        """
        self.colour_box.configure(
            background="#FF0000", 
            width="10", 
            height="5"
        )
        self.colour_box.grid(row=0, column=0)

    def adjust_window(self):
        """
            Sets the properties of the window of the application.
        """
        self.root.title("Chrispy Colour Palette")
        self.root.iconbitmap("favicon.ico")
        self.root.configure(
            bg="#1D1D1D", 
            padx="15", 
            pady="25"
        )

    def render_hex_frame(self):
        """
            Renders the section that is for hex value input.
        """
        self.hex_frame.configure(
            bg="#1D1D1D", 
            fg="#FFFFFF",
            padx=10,
            pady=4
        )
        self.hex_frame.grid(row=1, column=0)

    def render_hex_label(self):
        """
            Renders the label for the hex value input.
        """
        self.hex_label.configure(
            bg="#1D1D1D", 
            fg="#FFFFFF"
        )
        self.hex_label.grid(row=1, column=0)

    def render_hex_input(self):
        """
            Renders the input box for hex inputs
        """
        self.hex_input.configure(
            width=8,
        )
        self.hex_input.grid(row=1, column=1)

    def render_rgb_frame(self):
        """
            Renders the section that is for RGB value input.
        """
        self.rgb_frame.configure(
            bg="#1D1D1D", 
            fg="#FFFFFF",
            padx=10,
            pady=4
        )
        self.rgb_frame.grid(row=2, column=0)
        
    def render_rgb_colour_labels(self):

        labels = [self.red_label, self.green_label, self.blue_label]
        column_counter = 0

        for label in labels:
            label.configure(
                bg="#1D1D1D", 
                fg="#FFFFFF"
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
                width=4
            )
            colour_input.grid(row=0, column=column_counter)
            column_counter += 2

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

        self.set_initial_values()
        self.root.mainloop()

    def hex_updated(self, event):
        try:
            hex_value = self.hex_input.get()
            self.colour_box.configure(
                background=f"#{hex_value}", 
            )
            rgb_values = ColourConverter().convert_hex_to_rgb(f"#{hex_value}")
            self.red_input.delete(0, "end")
            self.red_input.insert(0,rgb_values[0])
            self.green_input.delete(0, "end")
            self.green_input.insert(0, rgb_values[1])
            self.blue_input.delete(0, "end")
            self.blue_input.insert(0, rgb_values[2])
        except Exception:
            pass

    def rgb_updated(self, event):
        try:
            red = int(self.red_input.get())
            green = int(self.green_input.get())
            blue = int(self.blue_input.get())
            hex_value = ColourConverter().convert_rgb_to_hex(red, green, blue)
            self.colour_box.configure(
                background=f"#{hex_value}", 
            )
            self.hex_input.delete(0, "end")
            self.hex_input.insert(0, hex_value)
        except Exception:
            pass

Renderer().render()
