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
        self.hex_input.bind("<KeyRelease>", self.update_hex)

        self.rgb_frame = tk.LabelFrame(self.root, text="RGB")
        self.red_label = tk.Label(self.rgb_frame, text="Red:")
        self.red_input = tk.Entry(self.rgb_frame)
        self.red_input.bind("<KeyRelease>", self.update_rgb)
        self.green_label = tk.Label(self.rgb_frame, text="Green:")
        self.green_input = tk.Entry(self.rgb_frame)
        self.green_input.bind("<KeyRelease>", self.update_rgb)
        self.blue_label = tk.Label(self.rgb_frame, text="Blue:")
        self.blue_input = tk.Entry(self.rgb_frame)
        self.blue_input.bind("<KeyRelease>", self.update_rgb)

        self.clipboard_image = ImageTk.PhotoImage(Image.open("./clipboard.png").resize((30,30)), Image.ANTIALIAS)
        self.input_boxes = {
            "red": self.red_input,
            "green": self.green_input,
            "blue": self.blue_input,
            "hex": self.hex_input
        }

        self.hex_clipboard_button = tk.Button(self.hex_frame, image=self.clipboard_image, command=lambda: Clipboard().copy_to_clipboard(self.root, self.input_boxes, "hex"))
        self.rgb_clipboard_button = tk.Button(self.rgb_frame, image=self.clipboard_image, command=lambda: Clipboard().copy_to_clipboard(self.root, self.input_boxes, "rgb"))

        self.colours = {
            "invalid input": "#FF726F",
            "default background": "#1D1D1D",
            "secondary": "#FFFFFF",
            "colour box": "#FF0000"
        }

        self.default_font_size = 14

    def update_hex(self, event):
        """
            The method that is called when the hex input box has been updated.
        """
        InterfaceUpdater().hex_updated(self.input_boxes, self.colour_box, self.colours)

    def update_rgb(self, event):
        """
            The method that is called when a RGB box has been updated.
        """
        InterfaceUpdater().rgb_updated(self.input_boxes, self.colour_box, self.colours)

    def render_colour_box(self):
        """
            Renders the box that shows the colour
        """
        self.colour_box.configure(
            width=14, 
            height=7
        )
        InterfaceUpdater.update_colour_box(self, self.colour_box, self.colours)
        self.colour_box.grid(row=0, column=0)

    def adjust_window(self):
        """
            Sets the properties of the window of the application.
        """
        self.root.title("Chrispy Colour Palette")
        self.root.iconbitmap("favicon.ico")
        self.root.resizable(False, False)
        self.root.configure(
            bg=self.colours["default background"], 
            padx=15, 
            pady=25,
        )

    def render_hex_frame(self):
        """
            Renders the section that is for hex value input.
        """
        self.hex_frame.configure(
            bg=self.colours["default background"], 
            fg=self.colours["secondary"],
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
            bg=self.colours["default background"], 
            fg=self.colours["secondary"],
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
            bg=self.colours["default background"], 
            fg=self.colours["secondary"],
            font=self.default_font_size,
            padx=10,
            pady=4
        )
        self.rgb_frame.grid(row=2, column=0)
        
    def render_rgb_colour_labels(self):
        """
            Renders the labels for red, green and blue inputs
        """
        labels = [self.red_label, self.green_label, self.blue_label]
        column_counter = 0

        for label in labels:
            label.configure(
                bg=self.colours["default background"], 
                fg=self.colours["secondary"],
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
        """
            Renders the clipboard button
        """
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

Renderer().render()