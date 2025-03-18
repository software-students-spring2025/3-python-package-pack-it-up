![Python build & test](https://github.com/software-students-spring2025/3-python-package-pack-it-up/actions/build.yaml/badge.svg)

# Python Package Example

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
python -m src.commitPackage --random

python -m src.commitPackage --style funny
python -m src.commitPackage --style serious
python -m src.commitPackage --style professional
python -m src.commitPackage --style technical

python -m src.commitPackage --blame

python -m src.commitPackage --haiku

python -m src.commitPackage --addMessage funny "Fixed a typo"
python -m src.commitPackage --addMessage serious "Refactored database access layer"
python -m src.commitPackage --addMessage chaotic "DO NOT DELETE - I'm warning you"

python -m src.commitPackage --addExcuse "The intern wrote this line"

python -m src.commitPackage --addHaiku "Branches intertwine, Merge conflicts are poetry, Git writes our stories."
```






## Running [`exampleProgram.py`](exampleProgram.py)

To run [`exampleProgram.py`](exampleProgram.py), make sure you are in your virtual environment and have all dependencies installed. Then, run the following command:

```bash
python exampleProgram.py
```


