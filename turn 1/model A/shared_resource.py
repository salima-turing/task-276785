import unittest


class TestSensitivityLevels(unittest.TestCase):

    def setUp(self):
        self.counter = 0

    def test_increment_counter(self):
        self.counter += 1
        self.assertEqual(self.counter, 1)
if __name__ == '__main__':
    unittest.main(parallel=2)
