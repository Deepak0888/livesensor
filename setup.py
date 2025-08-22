from setuptools import find_packages,setup
from typing import List


def get_requirements() -> list[str]:

    requiremnts_list = list[str] = []

    return requiremnts_list

setup(
    name = "livesensor",
    version="0.0.1",
    author="deepak0888",
    author_email="deepaku0222@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
    )


