import os
from setuptools import find_packages, setup

def read(fname):
    '''
    Utility function to read the README file.
    Used for the long_description.
    '''
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mobility_data_converter',
    packages=['src'],
    version='0.1.0',
    description='Convert data from CAMs to a format compatible with the simulator. ',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md'),
                              encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Ana',
    license='MIT',
)
