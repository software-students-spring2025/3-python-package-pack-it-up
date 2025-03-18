import argparse
from src.commitPackage.lazyCommit import (
    generate_commit_message, random_commit_message,
    git_blame_excuse, generate_haiku, add_commit_message, add_excuse, add_haiku
)

def example_program():
    print("Example Program: Demonstrating all functionalities...\n")

    # Random commit message
    print("Random commit message:")
    print(random_commit_message())

    # Generate commit message with specific style
    print("\nFunny commit message:")
    print(generate_commit_message('funny'))

    # Get a funny git blame excuse
    print("\nGit blame excuse:")
    print(git_blame_excuse())

    # Generate Haiku-style commit message
    print("\nHaiku commit message:")
    print(generate_haiku())

    # Add commit message to a style
    print("\nAdding a new commit message to 'funny' style:")
    print(add_commit_message('funny', 'Example Program Commit Message'))

    # Add a git excuse
    print("\nAdding a new git excuse:")
    print(add_excuse('Example Program Excuse'))

    # Add a haiku
    print("\nAdding a new haiku:")
    print(add_haiku('Example Program Haiku'))

if __name__ == "__main__":
    example_program()
