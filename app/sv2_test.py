import unittest
from sv2_new import service_2

class TestSv1(unittest.TestCase):
    def test_sv2(self):
        result = service_2()
        self.assertEqual(result, 9)

if __name__ == "__main__":
    unittest.main()