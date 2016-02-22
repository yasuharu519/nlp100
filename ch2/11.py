#!/usr/bin/env python

import sys


def main():
    filename = sys.argv[1]
    print ''.join([x if x is not '\t' else ' ' for x in open(filename).read()])

if __name__ == "__main__":
    main()
