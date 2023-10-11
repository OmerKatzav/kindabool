from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='kindabool',
    description='A python package for things that are only kinda true.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='1.0.0',
    license='MIT',
    author="kamudi",
    packages=find_packages(),
    url='https://github.com/kamudi/kindabool',
    keywords='bool boolean kindabool kinda_bool kinda_boolean',
)
