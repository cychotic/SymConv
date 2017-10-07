#!/usr/bin/env python
from math import log


def convert(symbols, list_x, list_y):
    """Converts symbols from list_x to list_b

    :param symbols: Symbols to be converted
    :param list_x: Symbols X set
    :param list_y: Symbols Y set
    :return: Converted symbols
    """

    master_x = list(filter(lambda a: a != '' and a != ' ', list_x))
    if len(master_x) != len(set(master_x)):
        raise ValueError("Values in set are not unique")
    master_y = list(filter(lambda a: a != '' and a != ' ', list_y))
    if len(master_y) != len(set(master_y)):
        raise ValueError("Values in set are not unique")
    old_symbols = list(filter(lambda a: a != '' and a != ' ', symbols))

    value = 0
    len_x = len(master_x)
    for x in range(len(old_symbols)):
        value *= len_x
        value += master_x.index(old_symbols[x])

    new_symbols = []
    len_y = len(master_y)
    loop = log(len(master_x)**len(old_symbols), len(master_y))
    if not loop.is_integer():
        raise ValueError("Symbol list sizes not compatible")
    num = value
    for x in range(int(loop)):
        new_symbols.insert(0,master_y[num % len_y])
        num = num // len_y

    return new_symbols

if __name__ == '__main__':

    from random import SystemRandom

    alphabet = '9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    generator = SystemRandom()

    def test():
        syms = list(generator.choice(alphabet) for _ in range(81))

        with open('symbols.txt', 'r') as f:
            symbols = f.read().splitlines()

        with open('words.txt', 'r') as f:
            words = f.read().splitlines()

        return convert(convert(syms,symbols,words),words,symbols) == syms

    for x in range(100):
        if not test():
            print("Test failed")
            exit(1)
    print("Test passed")
