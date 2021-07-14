def same(f,g):
    return lambda x,y : f(x) == g(y)


a = lambda x: x + 1
b = lambda y: y + 1

print(same(a,b)(1,2))
