from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Colorectal Cancer Prediction Project",
    version="0.1",
    author="Manish",
    packages=find_packages(),
    install_requires = requirements,
)