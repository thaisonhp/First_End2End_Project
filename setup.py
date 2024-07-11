from setuptools import find_packages,setup 
from typing import List 

HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str)->List[str]:
    '''
    this function will return the list of requirement 
    '''
    requirement = [] 
    with open(file_path) as file_obj : 
        requirements = file_obj.readlines() 
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements : 
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name = "E2Eproject",
    version = "0.0.1",
    author="Luong thai son",
    author_email= "luongthaison@gmail.com",
    packages = find_packages() , 
    install_requies = get_requirement('requirement.txt')
)