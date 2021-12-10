import unittest
from kmp import *


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(kmp("bbbbbbbbbbb","aaaaaaaaaaa"), False)




if __name__ == "__main__":
    unittest.main()
