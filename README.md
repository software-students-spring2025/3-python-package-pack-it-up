[![CI](https://github.com/software-students-spring2025/3-python-package-pack-it-up/actions/workflows/build.yml/badge.svg)](https://github.com/software-students-spring2025/3-python-package-pack-it-up/actions/workflows/build.yml)

# LazyCommit Package

## Team Members

1. [Jasmeen Kaur](https://github.com/jk7297)
2. [Sophia Schlichting](https://github.com/schlichtings)
3. [Preston Lee](https://github.com/prestonglee0805)
4. [Julia Ahn](https://github.com/juliaahn)

## About LazyCommit

A fun and lighthearted package for generating random and styled Git commit messages.

# Team Members

Jasmeen Kaur
[Sophia Schlichting](https://github.com/schlichtings)<br/>  
Preston Lee
[Julia Ahn](https://github.com/juliaahn)<br/>

## Usage

Import the package and use the following functions:

```
from src.commitPackage.lazyCommit import (
    generate_commit_message, random_commit_message,
    git_blame_excuse, generate_haiku, add_commit_message, add_excuse, add_haiku
)

print(random_commit_message())
#Output: Random commit message from the database

print(generate_commit_message('funny'))
#Output: Random commit message with the specific style

print(git_blame_excuse())
#Output: Random excuse from database

print(generate_haiku())
#Output: Random haiku from the database

print(add_commit_message('funny', 'Example Program Commit Message'))
#Output: Add commit message to a style

print(add_excuse('Example Program Excuse'))
#Output: Add an excuse to the database

print(add_haiku('Breeze whispers through trees, Golden leaves dance on the wind, Autumn's soft embrace.'))
#Output: Add a haiku to the databse
```

Or try running the package as a script:

```
python -m commitPackage --random

python -m commitPackage --style funny
python -m commitPackage --style serious
python -m commitPackage --style professional
python -m commitPackage --style technical

python -m commitPackage --blame

python -m commitPackage --haiku

python -m commitPackage --addMessage funny "Fixed a typo"
python -m commitPackage --addMessage serious "Refactored database access layer"
python -m commitPackage --addMessage chaotic "DO NOT DELETE - I'm warning you"

python -m commitPackage --addExcuse "The intern wrote this line"

python -m commitPackage --addHaiku "Branches intertwine, Merge conflicts are poetry, Git writes our stories."
```

## Running [`exampleProgram.py`](exampleProgram.py)

To run [`exampleProgram.py`](exampleProgram.py), make sure you are in your virtual environment and have all dependencies installed. Then, run the following command:

```bash
python exampleProgram.py
```


