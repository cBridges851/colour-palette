import unittest
from colour_converter import ColourConverter

class TestColourConverter(unittest.TestCase):
    def test_convert_hex_to_rgb_six(self):
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#FFFFFF"), [255, 255, 255])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#000000"), [0, 0, 0])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#112233"), [17, 34, 51])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#AABBCC"), [170, 187, 204])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#11BBCC"), [17, 187, 204])
        
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#2955C0"), [41, 85, 192])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#32A852"), [50, 168, 82])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#EB4034"), [234, 64, 52])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#4287F5"), [66, 135, 245])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#FCBA03"), [252, 186, 3])
    
    def test_convert_hex_to_rgb_three(self):
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#FFF"), [255, 255, 255])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#000"), [0, 0, 0])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#123"), [17, 34, 51])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#ABC"), [170, 187, 204])
        self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("#1BC"), [17, 187, 204])


    # def test_without_hashtags(self):
    #     self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("FFFFFF"), [255, 255, 255])
    #     self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("FFFF"), [255, 255, 255])
    #     self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("FFF"), [255, 255, 255])
    #     self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("000000"), [0, 0, 0])
    #     self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("0000"), [0, 0, 0])
    #     self.assertAlmostEqual(ColourConverter().convert_hex_to_rgb("000"), [0, 0, 0])



    # def test_convert_rgb_to_hex(self):
    #     self.assertAlmostEqual(1, 2)