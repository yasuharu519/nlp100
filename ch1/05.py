#!/usr/bin/env python
# coding: utf-8

STR="I am an NLPer"

def word_ngram(str_, n):
    return [x for x in zip(
        *[str_.split()[x:] for x in xrange(n)])]

def char_ngram(str_, n):
    return [x for x in zip(
        *[str_[x:] for x in xrange(n)])]

def main():
    print word_ngram(STR, 3)
    print char_ngram(STR, 3)

if __name__ == '__main__':
    main()
