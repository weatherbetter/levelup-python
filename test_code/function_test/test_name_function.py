import unittest
from name_function import get_full_name

class NamesTestCase(unittest.TestCase):
    """name_function.py 테스트"""

    def test_first_last_name(self):
        """just first, last name not middle
        """
        full_name = get_full_name("hong")
        self.assertEqual(full_name, "Hong Dong")

if __name__ == "__main__":
    unittest.main()