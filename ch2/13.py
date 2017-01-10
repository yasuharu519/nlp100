#!/usr/bin/env python

import sys

def main():
    with open('col1.txt') as col1, open('col2.txt') as col2:
        line = zip([x.strip() for x in col1.readlines()],
                [x.strip() for x in col2.readlines()])
        for l in line:
            print "{}\t{}".format(l[0], l[1])

if __name__ == "__main__":
    main()
