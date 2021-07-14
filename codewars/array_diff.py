def array_diff(a, b):
    lst = []
    for num in a:
        if num not in b:
            lst += [num]
    return lst








print(array_diff([19, -17, -17, 17, -3, -3, -10, -11, -7, 19, -11, -17, 0, -9, -14, 18, 11], [-15, -3, -6, 19, 0, -14, 16, -3, -10, 0, 20, -8, -9, 9, -5, 7, 15, 20, 4, 10]))
