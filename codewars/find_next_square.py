def find_next_square(sq):
    a = sq ** 0.5
    c = str(a)
    b = c.split(".")
    if b[1] == "0":
        d = b[0]
        e = int(d)
        return (e + 1) ** 2
    return -1
#or just check with a % 1 non quadratic nums have rest
print(find_next_square(114))
