def one(f=None):
    if f is None:
        return 1
    else:
        return f(1)

def two(f=None):
    if f is None:
        return 2
    else:
        return f(2)

def add(y):
    return lambda x: x +y

print(one(add(two())))
