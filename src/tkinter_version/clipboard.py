class Clipboard:
    def copy_to_clipboard(self, root, input_boxes, mode):
        root.clipboard_clear()

        if mode == "hex":
            root.clipboard_append(f"#{input_boxes['hex'].get()}")
        else:
            root.clipboard_append(f"{input_boxes['red'].get()}, {input_boxes['green'].get()}, {input_boxes['blue'].get()}")