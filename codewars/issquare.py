def is_square(n):
    a = n ** 0.5
    b = str(a)
    c = b.split(".")
    print(c)
    return True if c[1] == '0' else False

print(is_square(25))
