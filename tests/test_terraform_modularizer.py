import unittest
import sys
sys.path.append('./src')
from terraform_modularizer.modularize import parsehcl
from terraform_modularizer.help_messages import help_messages

class TestTerraformModularizerMethods(unittest.TestCase):

    def test_parsehcl_success(self):
        """parsehcl succeeds with a valid terraform file"""
        expected_data = {
            'resource': [{
                'aws_instance': {
                    'the_machine': {
                        'ami': ['ami-12345'],
                        'instance_type': ['t2.micro'],
                        'availability_zone': ['us-east-1a'],
                        'subnet_id': ['subnet-11zxcvxcv'],
                        'vpc_security_group_ids': [[
                            '${aws_security_group.the_group.id}',
                            '${aws_security_group.the_other_group.id}'
                        ]],
                        'tags': [{'Terraform': True}]
                    }
                }
            }]
        }
        parsed_data = parsehcl('tests/test_good.tf')
        self.assertIsInstance(parsed_data, dict)
        self.assertEqual(expected_data, parsed_data)

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
