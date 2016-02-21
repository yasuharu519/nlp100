#!/usr/bin/env python
# coding: utf-8

import random

STR="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def shuf(str_):
    a = list(str_)
    random.shuffle(a)
    return "".join(a)

def convert(str_):
    return " ".join(
            [x if len(x) <= 4 else "".join(
                x[0] + shuf(x[1:-1]) + x[-1]) for x in str_.split()])

def main():
    print convert(STR)

if __name__ == '__main__':
    main()
