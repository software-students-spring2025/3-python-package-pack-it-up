import argparse
from lazyCommit import generate_commit_message, random_commit_message, git_blame_excuse

def main():
    parser = argparse.ArgumentParser(description="LazyCommit: Generate commit messages easily!")
    
    parser.add_argument("--style", type=str, help="Generate a commit message with a specific style (funny, serious, chaotic)")
    parser.add_argument("--random", action="store_true", help="Generate a completely random commit message")
    parser.add_argument("--blame", action="store_true", help="Get a funny git blame excuse")
    
    args = parser.parse_args()

    if args.style:
        print(generate_commit_message(args.style))
    elif args.random:
        print(random_commit_message())
    elif args.blame:
        print(git_blame_excuse())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
