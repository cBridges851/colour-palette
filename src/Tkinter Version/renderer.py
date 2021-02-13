import tkinter as tk

class Renderer():
    def __init__(self):
        self.root = tk.Tk()

    def render(self):
        self.root.mainloop()

Renderer().render()