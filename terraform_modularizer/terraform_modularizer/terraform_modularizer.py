import sys
import argparse
import subprocess
import hcl2
from terraform_modularizer.help_messages import help_messages
from lark.exceptions import UnexpectedToken

# ANSI escape sequences for foreground text colors
red = '\033[31m'
nocolor = '\033[0m'
"""shell_args_resource = [
    'terraform',
    'state',
    'mv',
    f'{hcl_object_type}.{resource_name}',
    f'module.{module}',
    ]
shell_args_module = [
    'terraform',
    'state',
    'mv',
    f'module.{hcl_object_type}',
    f'module.{module}.module.{hcl_object_type}',
    ]"""


def parseargs():
    """Parses command line arguments"""

    parser = argparse.ArgumentParser(
        description=help_messages['parser_description'])
    parser.add_argument(
        "resources_file",
        help=help_messages['resources_help'])
    parser.add_argument(
        "module",
        help=help_messages['module_help'].format(red, nocolor))

    return parser.parse_args()


def parsehcl(resources_file):
    """Parses the HCL in a Terraform config file"""

    try:
        with(open(resources_file, 'r')) as f:
            return hcl2.load(f)
    except FileNotFoundError:
        print(help_messages['no_terraform'].format(resources_file))
        sys.exit(1)
    except UnexpectedToken:
        print(help_messages['invalid_terraform'])
        sys.exit(1)


def terraform_mv(shell_args):
    """Moves the state of the Terraform objects to the module"""

    print("Trying '", end='')
    for term in shell_args:
        print(term, end=' ')
    print("'\n")

    try:
        print(subprocess.run(
            args=shell_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            timeout=10, check=True, text=True).stdout)
        return 1
    except subprocess.CalledProcessError as e:
        print(
            'The Terraform CLI says:',
            e.stdout)
            #str(e.stderr,'utf-8'))


def modularize(resources_file, module):
    """Moves state to child module

    Moves the state of all resource and module objects to the specified
    module
    """

    # only resources and modules have state and need to be moved
    hcl_objects = [
        'resource',
        'module',
        ]

    hcl_objects_parsed = parsehcl(resources_file)

    for hcl_object in hcl_objects:
        for hcl_object_types in hcl_objects_parsed.get(hcl_object, []):
            for hcl_object_type in hcl_object_types.keys():
                if hcl_object == hcl_objects[0]:
                    for resource_name in hcl_object_types[hcl_object_type].keys():
                        shell_args = [
                            'terraform',
                            'state',
                            'mv',
                            f'{hcl_object_type}.{resource_name}',
                            f'module.{module}']
                        terraform_mv(shell_args)
                elif hcl_object == hcl_objects[1]:
                    shell_args = [
                        'terraform',
                        'state',
                        'mv',
                        f'module.{hcl_object_type}',
                        f'module.{module}.module.{hcl_object_type}']
                    terraform_mv(shell_args)
