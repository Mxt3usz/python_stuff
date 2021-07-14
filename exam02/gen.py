def take(n:int,xs):
    for x in xs:
        if x < n:
            yield x



print(list(take(3,range(7))))


a = lambda x: x>0

def myfilter(f,xs):
    for x in xs:
        if f(x) == True:
            yield x


print(list(myfilter(a,range(-5,8))))

