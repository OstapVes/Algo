import unittest
from electr import *


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(same_one([[1,4],[1,4],[1,4]],0,3), 10)




if __name__ == "__main__":
    unittest.main()