#lst = [1,2,3,4,5]
#a = [lst[i] >= lst[i-1] for i in range(1,len(lst))]

def is_sorted(lst):
    b = None
    for x in lst:
        for y in lst[::-1]:
            if x <= y:
                b = True
            else:
                b = False # here we return cuz no sense in looking further
                return b
            if lst.index(x) == lst.index(y): # means left and right meet
                break
    return b

#print(is_sorted(lst))
lst=[1,0,1,0]
bits_to_int = [2 ** (len(lst) - 1 - i) for i in range(len(lst)) if lst[i] == 1]
print(sum(bits_to_int))
is_sorted = lambda xs: all(xs[i] <= xs[j] for i in range(0, len(xs))
                                          for j in range(i, len(xs)))

