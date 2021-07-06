def to_binary(n:int):
    lst = []
    if n == 0:
        lst.append(n)
    while n > 0:
        lst .append(n%2)
        n  //= 2
    return lst[::-1]

print(to_binary(13))
print(to_binary(0))
print(to_binary(10))

def verify(data:int,checksum :int)->bool:
    lst = to_binary(data)
    summed = sum(lst)
    if summed % 2 == 1 and checksum == 1 or summed % 2 == 0 and checksum == 0:
        return True
    else:
        return False

print(verify(13,1))
print(verify(13,0))
print(verify(10,0))
print(verify(10,1))
