#!/usr/bin/env python

import string

def cipher(str_):
    return "".join([x if x not in string.ascii_lowercase else chr(219 - ord(x)) for x in str_])

def main():
    print cipher("aAa23dafa")

if __name__ == '__main__':
    main()
