import unittest
from colour_converter import ColourConverter

class TestColourConverterHexToRGB(unittest.TestCase):
    def test_six_units_output(self):
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#FFFFFF"), [255, 255, 255])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#000000"), [0, 0, 0])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#112233"), [17, 34, 51])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#AABBCC"), [170, 187, 204])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#11BBCC"), [17, 187, 204])
        
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#2955C0"), [41, 85, 192])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#32A852"), [50, 168, 82])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#EB4034"), [235, 64, 52])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#4287F5"), [66, 135, 245])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#FCBA03"), [252, 186, 3])
    
    def test_three_units_output(self):
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#FFF"), [255, 255, 255])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#000"), [0, 0, 0])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#123"), [17, 34, 51])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#ABC"), [170, 187, 204])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#1BC"), [17, 187, 204])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#BC9"), [187, 204, 153])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#B5E"), [187, 85, 238])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#45E"), [68, 85, 238])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#F12"), [255, 17, 34])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#5D6"), [85, 221, 102])

    def test_without_hashtags(self):
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("FFFFFF"), [255, 255, 255])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("000000"), [0, 0, 0])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("112233"), [17, 34, 51])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("AABBCC"), [170, 187, 204])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("11BBCC"), [17, 187, 204])
        
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("2955C0"), [41, 85, 192])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("32A852"), [50, 168, 82])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("EB4034"), [235, 64, 52])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("4287F5"), [66, 135, 245])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("FCBA03"), [252, 186, 3])

        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("FFF"), [255, 255, 255])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("000"), [0, 0, 0])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("123"), [17, 34, 51])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("ABC"), [170, 187, 204])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("1BC"), [17, 187, 204])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("BC9"), [187, 204, 153])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("B5E"), [187, 85, 238])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("45E"), [68, 85, 238])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("F12"), [255, 17, 34])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("5D6"), [85, 221, 102])

    def test_casing(self):
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#ABCDEF"), [171, 205, 239])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#abcdef"), [171, 205, 239])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("ABCDEF"), [171, 205, 239])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("abcdef"), [171, 205, 239])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#ABC123"), [171, 193, 35])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#abc123"), [171, 193, 35])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("ABC123"), [171, 193, 35])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("abc123"), [171, 193, 35])

    def test_invalid(self):
        # Lengths
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("ABC1234"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#ABC1234"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#ABCDEFG"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#1234567"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#ABCDE"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#12345"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#A2B4C"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#ABCD"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#1234"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#A2C4"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#AB"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#10"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#1F"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#A"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#0"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb(""), "Invalid")

        # Invalid characters
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#123AH4"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#PKLUTR"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#PKL"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#%A1"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#%A1456"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#%^$'#/"), "Invalid")

    def test_data_types(self):
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb(True), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb(False), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb(123456), [18, 52, 86])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb(1.3), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb({"a": 2}), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb(None), "Invalid")

class TestColourConverterRGBToHex(unittest.TestCase):
    def test_output(self):
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(255, 255, 255), "FFFFFF")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(0, 0, 0), "000000")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(208, 19, 126), "D0137E")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(35, 227, 59), "23E33B")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(104, 254, 238), "68FEEE")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(205, 75, 14), "CD4B0E")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(104, 108, 132), "686C84")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(61, 131, 121), "3D8379")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(116, 179, 26), "74B31A")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(165, 138, 69), "A58A45")

    def test_data_types(self):
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(3.3, 1.4, 12.3), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(True, False, True), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex("12", "32", "87"), "0C2057")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(12, 32, 87), "0C2057")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(-12, -32, -87), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex("A", "B", "C"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex("%", "4", "A"), "Invalid")
        self.assertAlmostEqual(ColourConverter().convert_rgb_to_hex(None, None, None), "Invalid")

    def test_number_of_parameters(self):
        self.assertRaises(TypeError, ColourConverter().convert_rgb_to_hex, 1)
        self.assertRaises(TypeError, ColourConverter().convert_rgb_to_hex, 1, 2)
        self.assertRaises(TypeError, ColourConverter().convert_rgb_to_hex, 1, 2, 3, 4)
