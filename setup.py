'''
The setup.py file is an essential part of packaging in Python. 
It contains information about the package, such as its 
name, version, description, author, and any dependencies required to install the package.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirement_lst:list[str]=[]
    try:
        with open('requirements.txt') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
    return requirement_lst

setup(
    name='NETWORKSECURITY',
    version='0.0.1',
    author='SAMEER MISHRA',
    author_email='sameermishra280202@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)