def get_sum(a,b):
    acc = 0
    if a > b:
        z = a
        a = b
        b = z
    if  a == b:
        return a
    if a < b:
        acc = 0
        for nums in range(a,b + 1):
            acc += nums
    return acc

print(get_sum(30,-6))
