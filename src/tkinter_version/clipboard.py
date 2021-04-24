class Clipboard:
    """
        The class that handles interaction with the clipboard
    """
    def copy_to_clipboard(self, root, input_boxes, mode):
        """
            The method that allows values on the program to be put onto
            the clipboard meaning they can be pasted elsewhere.
            Args:
                root: Tk, the original application
                input_boxes: object, contains all the input boxes in the application
                mode: string, informs the mode that is being inputted (i.e. hex or RGB)
        """
        root.clipboard_clear()

        if mode == "hex":
            root.clipboard_append(f"#{input_boxes['hex'].get()}")
        else:
            root.clipboard_append(f"{input_boxes['red'].get()}, {input_boxes['green'].get()}, {input_boxes['blue'].get()}")