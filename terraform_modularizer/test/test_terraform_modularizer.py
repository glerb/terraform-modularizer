import unittest
from terraform_modularizer.terraform_modularizer import parseargs, parsehcl
from terraform_modularizer.help_messages import help_messages

class TestTerraformModularizerMethods(unittest.TestCase):

    def test_parsehcl_filenotfound(self):
        """parsehcl fails when the file does not exist"""
        with self.assertRaises(SystemExit):
            parsehcl('nonexistent_file.tf')

    def test_parsehcl_unexpectedtoken(self):
        """parsehcl fails when the file contains invalid terraform"""
        with self.assertRaises(SystemExit):
            parsehcl('test/test.tf')

if __name__ == '__main__':
    unittest.main()
