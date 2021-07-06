
def parition(lst):
    p, rest = [0], [1:]
    l_lst = []
    h_lst = []
    for nums in rest:
        if nums <= p:
            l_lst += [nums]
        else:
            h_lst += [nums]
    return p, l_lst, h_lst


def quicksort(lst:list[int]):
    if len(lst) <= 1:
        return lst
    else:
        p, l_lst , h_lst = parition(lst)
        return(quicksort(l_lst) + [p] + quicksort(h_lst))
