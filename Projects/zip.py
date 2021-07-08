zz = zip(range(20),range(0,20,3))
print(list(zz))

a = range(20)
b= range(0,20,3)

def myZip(s1,s2):
    i1 = iter(s1)
    i2 = iter(s2)
    while True:
        e1 = next(i1)
        e2 = next(i2)
        yield(e1,e2)
zipped = myZip(a,b)
while True:
    print(next(zipped))
