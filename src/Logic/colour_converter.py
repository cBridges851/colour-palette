class ColourConverter:
    """
        Class responsible for converting hex values into RGB and vice versa.
    """

    def __init__(self):
        self.a = 10
        self.b = 11 
        self.c = 12
        self.d = 13
        self.e = 14
        self.f = 15
    
    def convert_hex_to_rgb(self, hex_value):
        """
            Method responsible for converting hex values into RGB.
            Args:
                hex_value: string, a colour represented with hexadecimal.
            Returns:
                rgb_values: list, each value for red, green and blue.
        """
        hex_value = str(hex_value)
        hex_value = hex_value.lstrip('#')
        
        if len(hex_value) == 6:
            red_hex = hex_value[0:2]
            green_hex = hex_value[2:4]
            blue_hex = hex_value[4:6]
        elif len(hex_value) == 3:
            red_hex = hex_value[0]
            green_hex = hex_value[1]
            blue_hex = hex_value[2]
        else:
            return "Invalid"

        rgb_values = [red_hex, green_hex, blue_hex]

        for i, item in enumerate(rgb_values):
            number_value = 0
            multiplier = 1
            value_length = len(rgb_values[i])
            
            if value_length == 1:
                rgb_values[i] = f"{rgb_values[i]}{rgb_values[i]}"
                value_length = 2

            while value_length > 0:
                current_unit = rgb_values[i][value_length - 1]

                if current_unit.isalpha():
                    current_unit = current_unit.upper()
                    
                    if current_unit == "A":
                        current_unit = self.a
                    elif current_unit == "B":
                        current_unit = self.b
                    elif current_unit == "C":
                        current_unit = self.c
                    elif current_unit == "D":
                        current_unit = self.d
                    elif current_unit == "E":
                        current_unit = self.e
                    elif current_unit == "F":
                        current_unit = self.f
                    else:
                        return "Invalid"
            
                if str(current_unit).isdigit() == False:
                    return "Invalid"

                number_value += int(current_unit) * multiplier
                multiplier = 16

                value_length -= 1

            rgb_values[i] = number_value
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
            if not str(number).isdigit():
                return "Invalid"
            
            current_hex_value = hex(int(number))
            current_hex_value = current_hex_value[2:].upper()
            
            if len(current_hex_value) == 1:
                current_hex_value = f"0{current_hex_value}"
            
            hex_colour_values.append(current_hex_value)

        return "".join(hex_colour_values)
