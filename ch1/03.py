#!/usr/bin/env python
# coding: utf-8

STR = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

def main():
    return [len(x) for x in STR.replace(',', '').split()]

if __name__ == '__main__':
    print main()
