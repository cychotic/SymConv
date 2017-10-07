#!/usr/bin/env python


def filterwords(filename):

    with open(filename, 'r') as f:
        words = f.read().splitlines()

    words = list(filter(lambda a: a != '' and a != ' ', words))  # remove blanks
    words = list(map(lambda a: a.lower(), words))  # change all lower case
    words = list(filter(lambda a: a.isalpha(), words))  # contains only alphanumeric
    words = list(filter(lambda s: len(s) == len(s.encode()), words))  # contains only ascii
    words = list(filter(lambda s: len(set(s))>1, words))  # contains only words with more than 1 characters, no 'aaa'
    words = list(filter(lambda s: len(s) > 4, words))  # more than 4 characters long
    words = list(set(words))  # contains only unique words
    words.sort()  # sort
    return words


def savefile(words, filename):
    f = open(filename, 'w')
    for x in words:
        f.write(x)
        f.write('\n')
    f.close()

