import argparse
from lazyCommit import generate_commit_message, random_commit_message, git_blame_excuse, generate_haiku, add_commit_message


def main():
    parser = argparse.ArgumentParser(
        description="LazyCommit: Generate commit messages easily!")

    parser.add_argument(
        "--style", type=str, help="Generate a commit message with a specific style (funny, serious, chaotic)")
    parser.add_argument("--random", action="store_true",
                        help="Generate a completely random commit message")
    parser.add_argument("--blame", action="store_true",
                        help="Get a funny git blame excuse")
    parser.add_argument("--haiku", action="store_true",
                        help="Generate a Haiku-style commit message")
    parser.add_argument(
        "--add", type=str, nargs=2, metavar=('style', 'message'),
        help="Add a commit message to a specific style. Requires style and message as arguments (e.g., --add funny 'Fixed a typo')")

    args = parser.parse_args()

    if args.add:
        style, message = args.add
        print(add_commit_message(style, message))
    elif args.style:
        print(generate_commit_message(args.style))
    elif args.random:
        print(random_commit_message())
    elif args.blame:
        print(git_blame_excuse())
    elif args.haiku:
        print(generate_haiku())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
