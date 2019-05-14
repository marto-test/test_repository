import unittest

import test_repository as awesome


class TestMethods(unittest.TestCase):
    def test_function_1(self):
        self.assertEqual(awesome.function_1(), True)


if __name__ == '__main__':
    unittest.main()
