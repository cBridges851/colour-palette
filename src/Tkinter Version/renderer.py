import tkinter as tk

class Renderer():
    def __init__(self):
        self.root = tk.Tk()

    def render_colour_box(self):
        colour_box = tk.Label()
        colour_box.config(background="#FF0000", width="10", height="5")
        colour_box.grid(row=0, column=0)

    def render_hex_section(self):
        hex_label = tk.Label(text="Hex:")
        hex_label.grid(row=1, column=0)

    def render(self):
        self.render_colour_box()
        self.render_hex_section()
        self.root.mainloop()

Renderer().render()