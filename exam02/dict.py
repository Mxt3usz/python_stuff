points = { "Maxi":[2,4,6], "Fabian":[3,7,2], "Arnold":[5,5,6]}


def total(points):
    new = {}
    for key,val in points.items():
        if sum(val) not in new:
            new.__setitem__(sum(val),[key])
        else:
            new[sum(val)] += [key]
    return new


print(total(points))
