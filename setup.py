from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' # keeping -e . in the requirements.txt will automatically trigger the setup.py file at the time of installation of the libraries.
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='MLProject',
version='0.0.1',
author='Pragn',
author_email='p3pragnpatel@gmail.com',
packages=find_packages(), # this will find the folders with __init__.py files and consider them as packages. 
install_requires=get_requirements('requirements.txt') 

)