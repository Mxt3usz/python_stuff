inc = lambda x: x + 1
mul2 = lambda x: x * 2

compose = lambda a,b: lambda x: a(b(x))

print(compose(inc,mul2)(4))
add = lambda a,b : a+b
print(add(5,4))
