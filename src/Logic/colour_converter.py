import matplotlib.colors as colors

class ColourConverter:
    def convert_hex_to_rgb(self, hex_value):
        percentage_values = colors.hex2color(hex_value)
        rgb_values = []

        for value in percentage_values:
            rgb_values.append(int(value * 255))

        return rgb_values

    def convert_rgb_to_hex(self, red, green, blue):
        hex_colour_values = []

        for number in red, green, blue:
            current_hex_value = hex(number)
            current_hex_value = current_hex_value[2:].upper()
            
            if len(current_hex_value) == 1:
                current_hex_value = f"0{current_hex_value}"
            
            hex_colour_values.append(current_hex_value)

        return "".join(hex_colour_values)
