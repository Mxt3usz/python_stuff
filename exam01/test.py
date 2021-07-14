import pytest
def letter_occurence(input :str)->str:
    chars = dict()
    for c in input:
        if not c.isupper() and not c.islower():
            return "error"
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    print(chars)
    maximum_doubling= max(chars.values())
    if maximum_doubling <= 1:
        return "einfach"
    elif maximum_doubling <= 2:
        return "doppelt"
    else:
        return "mehrfach"

print(letter_occurence("bbna"))
