import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='terraform-modularizer',
    version='0.1.0a1',
    author='P Z',
    author_email='',
    description="Moves state of existing Terraformed AWS resources",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/scribd/terraform-modularizer',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords='terraform module',
    packages=find_packages('src'),
    install_requires=['python-hcl2'],
    python_requires='>=3.8',
    package_data={'terraform-modularizer': ['help/*']}
)
