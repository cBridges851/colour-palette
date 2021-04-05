import tkinter as tk
from colour_converter import ColourConverter
from PySide2 import QtWidgets, QtGui
import os
import sys

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip("Chrispy Colour Palette")
        menu = QtWidgets.QMenu(parent)

        # Context Menu
        open_colour_palette = menu.addAction("Open palette")
        open_colour_palette.triggered.connect(self.open_colour_palette_app)
        
        _exit = menu.addAction("Exit")
        _exit.triggered.connect(lambda: sys.exit())

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.open_colour_palette_app)

    def open_colour_palette_app(self):
        Renderer().render()

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

        self.invalid_input_background = "#FF726F"

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
        hex_value = self.hex_input.get()
        rgb_values = ColourConverter().convert_hex_to_rgb(f"#{hex_value}")
        if rgb_values != "Invalid":
            self.hex_input.configure(
                background="#FFFFFF"
            )
            self.colour_box.configure(
                background=f"#{hex_value}", 
            )
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

        
        if red.isdigit() is False or int(red) > 255:
            self.red_input.configure(
                background=self.invalid_input_background
            )
            return
        
        if green.isdigit() is False or int(green) > 255:
            self.green_input.configure(
                background=self.invalid_input_background
            )
            return

        if blue.isdigit() is False or int(blue) > 255:
            self.blue_input.configure(
                background=self.invalid_input_background
            )
            return

        if red.isdigit() and green.isdigit() and blue.isdigit():
            self.red_input.configure(
                background="#FFFFFF"
            )
            self.green_input.configure(
                background="#FFFFFF"
            )
            self.blue_input.configure(
                background="#FFFFFF"
            )
            hex_value = ColourConverter().convert_rgb_to_hex(red, green, blue)
            self.colour_box.configure(
                background=f"#{hex_value}", 
            )
            self.hex_input.delete(0, "end")
            self.hex_input.insert(0, hex_value)
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("favicon.ico"), widget)
    tray_icon.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()