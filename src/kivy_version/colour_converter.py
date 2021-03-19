import matplotlib.colors as colors

class ColourConverter:
    """
        Class responsible for converting hex values into RGB and vice versa.
    """
    def convert_hex_to_rgb(self, hex_value):
        """
            Method responsible for converting hex values into RGB.
            Args:
                hex_value: string, a colour represented with hexadecimal.
            Returns:
                rgb_values: list, each value for red, green and blue.
        """
        percentage_values = colors.hex2color(hex_value)
        rgb_values = []

        for value in percentage_values:
            rgb_values.append(int(value * 255))

        return rgb_values

    def convert_rgb_to_hex(self, red, green, blue):
        """
            Method responsible for converting RGB values into hexadecimal.
            Args:
                red: int, the value representing the amount of red in a colour.
                green: int, the value representing the amount of green in a colour.
                blue: int, the value representing the amount of blue in a colour.
            Returns:
                string, the hex representation of the colour.
        """
        hex_colour_values = []

        for number in red, green, blue:
            current_hex_value = hex(number)
            current_hex_value = current_hex_value[2:].upper()
            
            if len(current_hex_value) == 1:
                current_hex_value = f"0{current_hex_value}"
            
            hex_colour_values.append(current_hex_value)

        return "".join(hex_colour_values)