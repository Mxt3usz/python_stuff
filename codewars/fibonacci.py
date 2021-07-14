def fibonacci(signature, n):
    for i in range(0,n - 2):
        new = signature[i] + signature[i + 1]
        signature += [new]
    return signature



print(fibonacci([1,1],6))#1,1,2,3,5,8
