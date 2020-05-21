import io
import unittest
import unittest.mock

from help_messages import help_messages
import terraform_modularizer

class TestTerraformModularizerMethods(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_parsehcl(self, mock_stdout):
        """check that parsehcl fails when the file does not exist"""
        fname = 'nonexistent_file.tf'

        with self.assertRaises(SystemExit) as e:
            terraform_modularizer.parsehcl(fname)
        self.assertEqual(e.exception.code, 1)
        expected_output = help_messages['no_terraform'].format(fname)
        # printing to stdout adds a newline; we shouldn't use print
        expected_output = f'{expected_output}\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
