#!/usr/bin/env python
# coding: utf-8

STR = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
IDX = [1, 5, 6, 7, 8, 9, 15, 16, 19]

def main():
    return dict([(i+1, word[:1]) if i+1 in IDX else (i+1, word[:2]) for i, word in enumerate(STR.split())])

if __name__ == '__main__':
    print main()
