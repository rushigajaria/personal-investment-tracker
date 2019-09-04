from calculate import sum_second

import unittest

class TestCalculateMethods(unittest.TestCase):

    def test_add_second(self):
        self.assertEqual(sum_second([(1,2),(3,4)]), 6)

if __name__ == '__main__':
    unittest.main()

