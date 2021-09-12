import unittest

import main


class MainTest(unittest.TestCase):
    def test_hellword(self):
        ret = main.helloword("Tets")
        self.assertEqual(ret, "ASDASD")


if __name__ == "__main__":
    unittest.main()
