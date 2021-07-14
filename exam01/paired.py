def paired(f,g):
    return lambda x,y: (f(x),g(y))

print(paired(lambda x: x * 2, lambda x: x * 3)(5,10))
