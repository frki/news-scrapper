import sys

from parser import parser


def main():
    args = parser()
    args.func(args.url, args.section)


if __name__ == "__main__":
    sys.exit(main())
