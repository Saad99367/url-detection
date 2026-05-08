"""
The setup.py file is an essential part of packaging and
distributing Python projects.
"""

from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """
    This function returns list of requirements
    """

    requirement_list = []

    try:

        with open('requirements.txt', 'r') as file:

            requirements = file.readlines()

            for req in requirements:

                req = req.strip()

                if req and req != "-e .":

                    requirement_list.append(req)

    except FileNotFoundError:

        print("requirements.txt file not found")

    return requirement_list


setup(
    name="url_detection_project",
    version="0.0.1",
    author="Saad Mohamed",
    packages=find_packages(),
    install_requires=get_requirements()
)