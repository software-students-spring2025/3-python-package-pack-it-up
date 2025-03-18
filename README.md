[![CI](https://github.com/software-students-spring2025/3-python-package-pack-it-up/actions/workflows/build.yml/badge.svg)](https://github.com/software-students-spring2025/3-python-package-pack-it-up/actions/workflows/build.yml)

# LazyCommit Package

## Team Members

1. [Jasmeen Kaur](https://github.com/jk7297)
2. [Sophia Schlichting](https://github.com/schlichtings)
3. [Preston Lee](https://github.com/prestonglee0805)
4. [Julia Ahn](https://github.com/juliaahn)

## About LazyCommit

A fun and lighthearted package for generating random and styled Git commit messages.

## PyPI Package Link

## Installation

## Usage

## Deveopment Guide

### Clone the Respository 

'''
git clone git@github.com:software-students-spring2025/3-python-package-pack-it-up.git
cd 3-python-package-pack-it-up
'''

### Set up Virtual Environment

'''
pip install pipenv
pipenv shell
'''

### Run Tests

Units test are provided in the tests directory. To run those use:
'''
python -m pytest 
'''

or  this if you have a python3:
'''
python3 -m pytest 
'''

### Build and Publish Package 

To build the package and upload it to TestPyPI:

```
python -m build
twine upload -r testpypi dist/*
```

To publish it to PyPI:
```
twine upload dist/*
```

## Contribute

To contribute to this project follow these steps:

1. Clone the repository
2. Create a feature branch 
```
git checkout -b feature-name.
```
3. Commit your changes 
```
git add .
git commit -m "Added new feature"
```
4. Push to your branch 
```
git push origin feature-name
```
5. Open a pull request.