#!/usr/bin/env python
if __name__ == '__main__':
    import sys
    from SymConv import convert

    with open('words.txt', 'r') as f:
        words = f.read().splitlines()

    with open('symbols.txt', 'r') as f:
        symbols = f.read().splitlines()

    print(" ".join(convert(sys.argv[1], symbols, words)))