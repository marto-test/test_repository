import unittest

import test_repository.test_module as awesome


class TestMethods(unittest.TestCase):
    def test_function_1(self):
        self.assertEqual(awesome.function_1(), True)

    def test_function_2(self):
        self.assertEqual(awesome.function_2(), True)


if __name__ == '__main__':
    unittest.main()
