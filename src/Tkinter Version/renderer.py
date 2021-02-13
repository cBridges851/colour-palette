import tkinter as tk

class Renderer():
    def __init__(self):
        self.root = tk.Tk()
        self.colour_box = tk.Label(self.root)

        self.hex_frame = tk.LabelFrame(self.root, text="Hex")
        self.hex_label = tk.Label(self.hex_frame, text="Hex:")
        self.hex_input = tk.Entry(self.hex_frame)

        self.rgb_frame = tk.LabelFrame(self.root, text="RGB")
        self.red_label = tk.Label(self.rgb_frame, text="Red:")
        self.red_input = tk.Entry(self.rgb_frame)
        self.green_label = tk.Label(self.rgb_frame, text="Green:")
        self.green_input = tk.Entry(self.rgb_frame)
        self.blue_label = tk.Label(self.rgb_frame, text="Blue:")
        self.blue_input = tk.Entry(self.rgb_frame)

    def render_colour_box(self):
        self.colour_box.config(background="#FF0000", width="10", height="5")
        self.colour_box.grid(row=0, column=0)

    def render_hex_frame(self):
        self.hex_frame.grid(row=1, column=0)

    def render_hex_label(self):
        self.hex_label.grid(row=1, column=0)

    def render_hex_input(self):
        self.hex_input.grid(row=1, column=1)

    def render_rgb_frame(self):
        self.rgb_frame.grid(row=2, column=0)
        
    def render_colour_labels(self):
        labels = [self.red_label, self.green_label, self.blue_label]
        column_counter = 0

        for label in labels:
            label.grid(row=0, column=column_counter)
            column_counter += 2

    def render_colour_inputs(self):
        colour_inputs = [self.red_input, self.green_input, self.blue_input]
        column_counter = 1

        for colour_input in colour_inputs:
            colour_input.grid(row=0, column=column_counter)
            column_counter += 2


    def render(self):
        self.render_colour_box()
        
        self.render_hex_frame()
        self.render_hex_label()
        self.render_hex_input()

        self.render_rgb_frame()
        self.render_colour_labels()
        self.render_colour_inputs()
        self.root.mainloop()

Renderer().render()