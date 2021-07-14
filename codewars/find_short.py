def find_short(s):
    a = s.split()
    b = 0
    for c in a:
        if b == 0:
            b = len(c)
        if b > len(c):
            b = len(c)
    return b




print(find_short("bitcoin take over the world maybe who knows perhaps"))
