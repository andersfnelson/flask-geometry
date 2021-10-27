import sphere
import unittest

class sphereTest(unittest.TestCase):
    def test_surface_area(self):
        assert(sphere.surface_area(0) == 0)
        assert(round(sphere.surface_area(5), 2) == 314.16)


    def test_volume(self):
        assert(sphere.volume(0) == 0)
        assert(round(sphere.volume(5), 2) == 523.6)



if __name__ == '__main__':
    unittest.main()