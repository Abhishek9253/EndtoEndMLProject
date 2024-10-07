from setuptools import setup, find_packages
from typing import List


Hypen_e_dot = "-e ."
def get_requirements(file_path)->List[str]:
    "This returns the list of requirements"
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

setup(
name='MlProject',
version='0.0.1',
author='Abhishek',
author_email='abhipanwar9253@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)