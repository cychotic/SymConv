#!/usr/bin/env python

if __name__ == '__main__':

    from random import SystemRandom
    from SymConv import convert

    alphabet = '9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    generator = SystemRandom()

    seed = list(generator.choice(alphabet) for _ in range(81))

    with open('symbols.txt', 'r') as f:
        symbols = f.read().splitlines()

    with open('words.txt', 'r') as f:
        words = f.read().splitlines()

    # verify seed before printing
    if convert(convert(seed, symbols, words), words, symbols) == seed:
        print("".join(seed))
        print(" ".join(convert(seed,symbols,words)))
    else:
        print("Generator failed. Do not use!")
