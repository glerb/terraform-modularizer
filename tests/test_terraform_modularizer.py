import unittest
import sys
sys.path.append('./src')
from terraform_modularizer.modularize import *
from terraform_modularizer.help_messages import help_messages

class TestTerraformModularizerMethods(unittest.TestCase):

    def test_parsehcl_success(self):
        """parsehcl succeeds with a valid terraform file"""
        self.assertIsInstance(parsehcl('tests/test_good.tf'), dict)

    def test_parsehcl_filenotfound(self):
        """parsehcl fails when the file does not exist. The following text is the error message a user sees:"""
        with self.assertRaises(SystemExit):
            parsehcl('nonexistent_file.tf')

    def test_parsehcl_unexpectedtoken(self):
        """parsehcl fails when the file contains invalid terraform. The following text is the error message a user sees:"""
        with self.assertRaises(SystemExit):
            parsehcl('tests/test_bad.tf')

if __name__ == '__main__':
    unittest.main()
