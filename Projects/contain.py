from typing import Any
import pytest
def contains(x: Any, xs: list[Any]) -> bool:
    if len(xs) == 0: #is first element?
        return False
    if xs[0] == x: #if empty return false
        return True
    else:
        return contains(x, xs[1:]) #if not first split list everytime

def test_1():
    assert(contains(1,[]) == False)

def test_2():
    assert(contains(2,[1,5,2]) == True)

def test_3():
    assert(contains(3,[2,1,5]) == False)
#print(contains(1,[]))


