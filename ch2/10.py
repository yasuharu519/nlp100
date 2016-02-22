#!/usr/bin/env python

import sys


def main():
    filename = sys.argv[1]
    print len(open(filename).readlines())

if __name__ == "__main__":
    main()
