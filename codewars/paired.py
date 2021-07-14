def paired(f,g):
    return lambda x,y: (f(x),g(y))

f = lambda x: x*2
g = lambda x: x*3

print(paired(f,g)(5,10))
