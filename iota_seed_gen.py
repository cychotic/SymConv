if __name__ == '__main__':

    from random import SystemRandom
    from SymConv import convert

    alphabet = '9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    generator = SystemRandom()

    syms = list(generator.choice(alphabet) for _ in range(81))

    with open('symbols.txt', 'r') as f:
        symbols = f.read().splitlines()

    with open('words.txt', 'r') as f:
        words = f.read().splitlines()

    print("".join(syms), " ".join(convert(syms,symbols,words)))
