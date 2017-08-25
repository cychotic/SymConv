# SymConv:

A symbol base converter.  It takes a set of symbols of X base, and converts it to symbols of Y base. Compatibility between the two sets of symbols is calculated as log( (base of X)^(length of symbols), (base of Y)) -> an integer.

Symbol sets are stored in text files.

### Example use case:

This can be used to convert 81 IOTA Seed of base 27 to 27 words of base 19683.  log(27^81, 19683) -> 27

### To Use:

`python seed_to_phrase.py 9ABCDEFGHIJKLMNOPQRSTUVWXYZ9ABCDEFGHIJKLMNOPQRSTUVWXYZ9ABCDEFGHIJKLMNOPQRSTUVWXYZ`

`python phrase_to_seed.py abbas bannet cebian dimple froise illude loligo nudge pulque abbas bannet cebian dimple froise illude loligo nudge pulque abbas bannet cebian dimple froise illude loligo nudge pulque`

### To Test:

`python symconv.py`
