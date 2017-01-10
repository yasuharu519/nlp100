#!/usr/bin/python

import sys


def main():
    if len(sys.argv) < 2:
        print("Please input N value")
        sys.exit(1)
    N = int(sys.argv[1])
    lines = [x.strip() for x in sys.stdin.readlines()[-N:]]
    print("\n".join(lines))

if __name__ == '__main__':
    main()
