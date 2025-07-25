from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='sb_perflog',
    version='0.1.2',
    packages=find_packages(),
    install_requires = [
        'pynvml==12.0.0',
        'psutil==7.0.0',
        'python-json-logger==3.3.0'
        ],
    long_description= description,
    long_description_content_type="text/markdown",
)