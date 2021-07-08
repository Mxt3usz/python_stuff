def upFrom(n:int):
    while n != 2:
        yield n
        n += 1
up = upFrom(0)

def downFrom(n:int):
    while True:
        yield n
        n -= 1
down = downFrom(10)

def gen(xs,ys):
    for x in xs:
        yield x
    for x in ys:
        yield x

generator = gen(up,down)
def take(n:int,xs):
    for i,x in enumerate(xs):
        if  i < n:
            yield x
        else:
            break
taked = take(4,up)


def chunks(n: int, xs):
    if n <= 0:
        while True:
            yield []
    chunk = []
    for x in xs:
        chunk.append(x)
        if len(chunk) == n:
            yield chunk
            chunk = []
    if len(chunk) > 0:
        yield chunk

def circle(xs):
    xs = list(xs)
    while True:
        for x in xs:
            yield x

hi = circle(up)
while True:
    print(next(hi))
