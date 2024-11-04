import unittest
import tempfile
import os


class TestSensitivityLevels(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_create_temp_file(self):
        temp_file_path = os.path.join(self.temp_dir.name, 'test_file.txt')
        with open(temp_file_path, 'w') as file:
            file.write("test data")

        self.assertTrue(os.path.exists(temp_file_path))


if __name__ == '__main__':
    unittest.main(parallel=2)
