#!/usr/bin/env python
# coding: utf-8

def main():
    str1 = u"パトカー"
    str2 = u"タクシー"
    print "".join([x + y for x, y in zip(str1, str2)]).encode('utf-8')

if __name__ == '__main__':
    main()
