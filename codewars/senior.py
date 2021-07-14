def open_or_senior(data):
    lst = []
    for a in range(0,len(data)):
        i = data[a]
        if i[0] >= 55 and i[1] > 7:
            lst += ["Senior"]
        else:
            lst += ["Open"]
    return lst




print(open_or_senior([[18,20],[45,2],[61,12],[37,6],[21,21],[78,9]]))
