
def dot_product(xs,ys):
                return sum(map(lambda x,y: x*y,xs,ys[::-1]))


print(dot_product([1,2,3,4], [10,20,30,40]) )


filtered = filter(lambda x: x>0,[2,3,4,5,-1])

print(list(filtered))

bits = lambda s: int(s,base=2)

print(bits("10001"))
from functools import reduce

reduced = reduce(lambda x,y: x*y,range(1,5))#accumlator is start point 1 1*2,2*3..i
print(reduced)
#or
def product(iterator):
    return reduce(lambda x,y: x*y,iterator,1)

print(product([2,3]))

filtered_string = map(lambda y: str(y), filter(lambda x: x%2==0,[2,7,8,10]))
print(list(filtered_string))
