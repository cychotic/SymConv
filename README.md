# SymConv:

A symbol base converter.  It takes a set of symbols of X base, and converts it to symbols of Y base. Compatibility between the two sets of symbols is calculated as log( (base of X)^(length of symbols), (base of Y)) -> an integer.

Symbol sets are stored in text files.

### Example use case:

This can be used to convert 81 IOTA Seed of base 27 to 27 words of base 19683.  log(27^81, 19683) -> 27

### To Use:

`python seed_to_phrase.py 9ABCDEFGHIJKLMNOPQRSTUVWXYZ9ABCDEFGHIJKLMNOPQRSTUVWXYZ9ABCDEFGHIJKLMNOPQRSTUVWXYZ`

`python phrase_to_seed.py abbas bannet cebian dimple froise illude loligo nudge pulque abbas bannet cebian dimple froise illude loligo nudge pulque abbas bannet cebian dimple froise illude loligo nudge pulque`

### To Test:

`python SymConv.py`

### To Randomly Generate a IOTA seed with phrase using SystemRandom:

`python iota_seed_gen.py`

### Note:

words.txt may change, if you are using the converter or generator, make sure you know which words.txt you are using.

### Warning:

Symbols used in words.txt and symbols.txt must be a UNIQUE set.

### To Customize:

You can modify words.txt/symbols.txt anyway you like.  But it must be a set with UNIQUE values.  The size of words.txt/symbols.txt must be compatible with each other.

wordutil.py contains functions that I used to filter out unwanted words.  Read the code to see the filters.