from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='terraform-modularizer',
    version='0.1.0',
    author='P Z',
    author_email='glerb@github.com',
    description="Batch moves state of existing Terraformed AWS resources",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/glerb/terraform-modularizer',
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X"
    ],
    keywords='terraform module state',
    install_requires=['python-hcl2'],
    python_requires='>=3.8',
)
