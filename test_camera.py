import unittest
from camera import Camera
import xmlrunner
testRunner=xmlrunner.XMLTestRunner(output='.')

class TestCamera(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')
        # return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        #   return super().tearDownClass()
        print()

    # create things/objects that'll be used in all the test
    # crete test directories/files that'll be used for testing
    def setUp(self):
        self.cam1 = Camera()

    # delete created things here.
    def tearDown(self):
        pass

    def test_hello(self):
            self.assertEqual(Camera.complex_logic(2), 4)

    def test_hello1(self):
            self.assertEqual(Camera.complex_logic(-2), 4)

    def test_hello2(self):
            self.assertEqual(Camera.complex_logic(0), 0)

if __name__ == '__main__':
    unittest.main(testRunner)