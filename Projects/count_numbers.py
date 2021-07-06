

def count_numbers(x:int,y:int,n:int):
    count = 0
    for numbers in range(x,n + 1):
        if numbers % x == 0 and numbers % y != 0:
            count += 1
    return count

print(count_numbers(2,5,10))
