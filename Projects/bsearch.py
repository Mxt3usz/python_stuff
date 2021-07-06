


from typing import Any, Optional


def bsearch(lst: list[Any], key: Any)->Any:
    mid = len(lst) // 2
    if len(lst) == 0:
        return None
    #print(lst[mid])
    if lst[mid] == key:
        return key
    if lst[mid] > key:
        return bsearch(lst[:mid],key)

    else:
        r = bsearch(lst[mid+1:],key)
        return None if r is None else r

def bsearch2(lst : list[int], key : int, lo:int, hi:int):
    mid = (lo + hi)//2
    if lo >= hi:
        return None
    if lst[mid] == key:
        return key
    if lst[mid] > key:
        return bsearch2(lst,key,lo,mid) #till the mid but without (mid - 1)
        #--> hi = mid
    else:
        return bsearch2(lst,key,mid + 1,hi) #without the mid
        #--> lo = mid + 1

lst = [3,5,7,10,15,17,20,29]
print(bsearch(lst,20))
