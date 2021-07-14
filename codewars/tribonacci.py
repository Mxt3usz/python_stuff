def tribonacci(signature, n):
    if n == 0:
        return []
    if n  == 1:
        return [signature[0]]
    if n == 2:
        return [signature[0]] + [signature[1]]
    for i in range(0, n - 3):
        new = signature[i] + signature[i + 1] + signature[i + 2]
        signature += [new]
    return signature








print(tribonacci([1, 1, 1], 2))
#[1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
