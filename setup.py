from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="Nexus OS",
    version="0.1.0",
    author="Subhanshu",
    author_email="subhanshu3070@gmail.com",
    description="AI-powered platform for financial report analysis, KPI extraction, risk scoring, and investment insights",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)