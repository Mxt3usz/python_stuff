def accumulate(xs):
    acc = 0
    for x in xs:
        acc += x
        yield acc



print(list(accumulate(iter([1,2,3,4,5,6]))))

def double(n : int) -> int:
    return n * 2

def my_map(f,xs):
    for x in xs:
        yield f(x)

print(list(my_map(double,iter([1,2,3,4]))))

def init(xs):
    for x in xs:
        if x is None:
            return []
        if x in xs[::-1]:
            yield x

print(list(init(iter([1,2,3,4]))))
