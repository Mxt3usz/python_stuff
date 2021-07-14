

def anagrams(word,words):
    lst = []
    for chars in words:
        lst += ["".join(sorted(chars))]
    res = []
    c = "".join(sorted(word))
    count = -1
    print("sorted:",lst)
    print("word",c)
    print("old:",words)
    for chars in lst:
        count += 1
        if c == chars:
            res += [words[count]]
    return res

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
