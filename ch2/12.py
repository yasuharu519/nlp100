#!/usr/bin/env python

import sys


def main():
    filename = sys.argv[1]
    header = []
    tail = []
    for line in open(filename).readlines():
        a, b = line.split()
        header.append(a)
        tail.append(b)
    with open('col1.txt', 'w') as col1:
        col1.write('\n'.join(header))
    with open('col2.txt', 'w') as col2:
        col2.write('\n'.join(tail))

if __name__ == "__main__":
    main()
