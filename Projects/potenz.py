def power(x: complex, n : int,acc:complex):
    if n == 0:
        return acc
    else:
        return power(x,n-1,acc * x)
        # x *power(x,n-1) geht auch

def power(x: complex, n : int):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(x*x,n//2)
    else:
        return x *power(x*x,n//2)

print(power(2,3))

print(power(2,3,1))
