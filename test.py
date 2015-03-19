import unittest
import rgb_to_hex


class TestRGBToHex(unittest.TestCase):

    def setUp(self):
        self.rgb_list = ['45,194,217', '00,00,00', '255,16,112', '255,255,255']

    def test_single_rgb_to_hex(self):
        hex_list = rgb_to_hex.get_hex_list(self.rgb_list[:1])

        self.assertEqual(['#2DC2D9'], hex_list)

    def test_rgb_list_to_hex(self):
        hex_list = rgb_to_hex.get_hex_list(self.rgb_list)

        self.assertEqual(['#2DC2D9', '#000000', '#FF1070', '#FFFFFF'],
                         hex_list)


if __name__ == '__main__':
    unittest.main()
