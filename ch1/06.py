#/usr/bin/env python
# coding: utf-8

STR1="paraparaparadise"
STR2="paragraph"

def char_ngram(str_, n):
    return [x for x in zip(
        *[str_[x:] for x in xrange(n)])]

def main():
    # 和集合
    add = set()
    add = add | set(char_ngram(STR1, 2))
    add = add | set(char_ngram(STR2, 2))
    print add
    # 積集合
    mul = set(char_ngram(STR1, 2))
    mul = mul & set(char_ngram(STR2, 2))
    print mul
    print "Included" if ('s', 'e') in set(char_ngram(STR1, 2)) and ('s', 'e') in set(char_ngram(STR2, 2)) else "Not Included"

if __name__ == '__main__':
    main()
