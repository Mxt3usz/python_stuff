def sum_quer(n:int):
    lst = [n]
    a = str(n)
    acc = 0
    count_x = 0
    count_y = 0
    for x in a:
        count_x += 1
        if acc != 0:
            lst += [acc]
            count_y = 0
        acc = 0
        for y in a:
            count_y += 1
            if count_y >= count_x:
                acc += int(y)
    return lst





print(sum_quer(25))
