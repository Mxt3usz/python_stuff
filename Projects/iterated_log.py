import math
def iterated_logarithm(n: float) -> int:
    if n <= 1:
        return 0
    else:
        count = 0
        while not n <= 1:
            count += 1
            n = math.log(n,2)
        return count

print(iterated_logarithm(1))
print(iterated_logarithm(16))
print(iterated_logarithm(16.7))
