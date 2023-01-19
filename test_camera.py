import unittest
from camera import Camera

class TestCamera(unittest.TestCase):

    def test_hello(self):
            self.assertEqual(Camera.complex_logic(2), 4)

    def test_hello1(self):
            self.assertEqual(Camera.complex_logic(-2), 4)

    def test_hello2(self):
            self.assertEqual(Camera.complex_logic(2.9), 8.41)

if __name__ == '__main__':
    unittest.main()