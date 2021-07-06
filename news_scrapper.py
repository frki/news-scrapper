import sys

from parser import parser


def main() -> int:
    args = parser()
    args.func(args.url, args.section)
    return 0

if __name__ == "__main__":
    sys.exit(main())
