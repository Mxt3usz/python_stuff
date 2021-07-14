def count_folds(width,height):
    count  = 0
    while True:
        if width > height:
            width //= 2
            count += 1
        if width < height:
            height //= 2
            count += 1
        if width == height:
            width //= 2
            count += 1
        if height == width:
            height //= 2
            count += 1
        if height == 0 or width == 0:
            break
    return count




print(count_folds(2,1))


