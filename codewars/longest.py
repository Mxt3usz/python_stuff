def longest(a1,a2):
    result = ""
    for c in a1:
        if c not in result:
            result += c
    for c in a2:
        if c not in result:
            result += c
    alpha = "abcdefghijklmnopqrstuvwxyz"
    sol = ""
    for x in alpha:
        if x in result:
            sol += x
    return sol
    #res = "".join(sorted(result))
    #return res
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a,b))
