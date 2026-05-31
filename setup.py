'''used by setup tools to define configuration of your project 
such as metadata dependencies and more
'''
from setuptools import find_packages,setup ### it find init.py file ND consider it package
from typing import List

def get_requirements()->List[str]:
    requirement_list:List[str] = []   # Initialize the list

    try:
        with open('requirements.txt','r')as file:
            #read line from file
            lines=file.readlines()

            #process each line
            for line in lines:
                requirement=line.strip()

                ##ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print('requirements.txt not found')

    return requirement_list


print(get_requirements())

setup(
    name="networksecurity",
    version="0.0.1",
    author='vedant',
    packages=find_packages(),
    install_requires=get_requirements(),
)

## -e . calls setup.py