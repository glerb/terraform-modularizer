from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='TerraformModularizer',
    version='0.1.0a1',
    author='P Z',
    author_email='',
    description="Batch moves state of existing Terraformed AWS resources",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/scribd/terraform-modularizer',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords='terraform module',
    install_requires=['python-hcl2'],
    python_requires='>=3.8',
)
