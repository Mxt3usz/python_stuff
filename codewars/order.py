def order(sentence):
    numbers = "123456789"
    d = sentence.split()
    res = []
    for a in numbers:
        for chars in d:
            if a in chars:
                res += [chars]
    return " ".join(res)




print(order("is2 Thi1s T4est 3a"))
