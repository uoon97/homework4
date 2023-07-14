import unittest
import sys
from sv1_new import service_1

class TestSv1(unittest.TestCase):
    def test_sv1(self):
        result = service_1()
        self.assertEquals(result, 1000)

if __name__ == "__main__":
    unittest.main()