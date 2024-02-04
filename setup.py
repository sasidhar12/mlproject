# This file used to build applicatipn as package 
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(path:str)->List[str]:
    '''
      This function will return the list of requirements
    '''
    requirements =[]
    with open(path,'r') as file:
        requirements = file.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="mlproject",
    version='0.0.1',
    author="sasidhar",
    author_email="durgasasidhar1234@gmail.com",
    packages=find_packages(),
    requires= get_requirements("requirements.txt")
)