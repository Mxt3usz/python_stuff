def is_scientific(s :str):
    count = 0
    for x in s:
        if x == "e":
            count += 1
    if count == 1:
        return True
    return False


print(is_scientific("3.0e5"))
print(is_scientific("3.0"))
