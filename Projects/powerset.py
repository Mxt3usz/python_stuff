"""
Implementation of the powerset
"""

def powerset(xs: list) -> list:
    """ Computes the power set of 'xs'."""
    if xs == []:
        return [[]]
    l1 = powerset(xs[1:])
    l2 = []
    for i in l1:
        l2.append([xs[0]] + i)
    return l1 + l2


print(powerset([1,2,3,4]))
