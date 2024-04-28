import unittest
from infija import infija_postfija

class TestIn(unittest.TestCase):
    def test_infija(self):
        result = infija_postfija("1+2")
        self.assertEqual(result, "12+")

if __name__ == '__main__':
    unittest.main()
    