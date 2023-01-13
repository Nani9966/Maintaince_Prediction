from setuptools import find_packages,setup
from typing import List

REQUIRMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements() ->List[str]:
    with open(REQUIRMENT_FILE_NAME) as requirment_file:
        requirment_list=requirment_file.readlines()
    requirment_list=[requirment_name.replace("\n", "") for requirment_name in requirment_list]
    
    if HYPHEN_E_DOT in requirment_list:
        requirment_list.remove(HYPHEN_E_DOT)
    return requirment_list






setup(
    name="MAINTAINCE",
    version="0.0.1",
    author="chinnareddy",
    author_email="chinnareddy2106@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)
