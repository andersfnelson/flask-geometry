import cone
import unittest

class coneTest(unittest.TestCase):
    def test_volume1(self):
        assert(cone.volume(2, 2) != 0)
    def test_volume2(self):
        assert(round(cone.volume(2, 2), 2) == 8.38)
    def test_surface_area(self):
        assert(round(cone.surface_area(2, 2), 2) == 30.34)
    def test_slant(self):
        assert(round(cone.slant(2, 2), 2) == 2.83)
    def test_lateral_surface_area(self):
        assert(round(cone.lateral_surface_area(2, 2), 2) == 17.77)


if __name__ == '__main__':
    unittest.main()