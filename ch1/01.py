#!/usr/bin/env python
# coding: utf-8

def main():
    idx = [1, 3, 5, 7]
    str_ = u"パタトクカシーー"
    print "".join(map(lambda x: str_[x], idx)).encode('utf-8')

if __name__ == '__main__':
    main()
