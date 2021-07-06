import sys

from parser import parser
import logging


def main() -> int:
    args = parser()
    args.func(args.url, args.section, args.debug)
    return 0


if __name__ == "__main__":
    sys.exit(main())
