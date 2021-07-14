def high_and_low(numbers):
    a = numbers.split(" ")
    high = 0
    low = 0
    res = ""
    print(a)
    for num in a:
        if high == 0 and low == 0:
            high = num
            low = num
        if int(low) > int(num):
            low = num
        if int(high) < int(num):
            high = num
    res += high + " "
    res += low
    return res


print(high_and_low("2038 -92 2531 1601 1263 1656 881 2319 2201 2973 854 837 1442 2006 2211 2622 1744 1151 -77 1264 2069 607"))
