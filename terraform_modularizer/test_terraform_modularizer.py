# couldn't figure out how unittest works, so this
# is my only attempt at writing a test

import unittest
import terraform_modularizer

class TestTerraformModularizerMethods(unittest.TestCase):

    def test_parsehcl(self):
        """check that parsehcl fails when the file does not exist"""
        with self.assertRaises(FileNotFoundError) as e:
            terraform_modularizer.parsehcl('nonexistent_file.tf')

if __name__ == '__main__':
    unittest.main()
