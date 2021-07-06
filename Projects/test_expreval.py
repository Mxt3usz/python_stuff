"""
Tests expreval
"""
from tree import Node, leaf
from expreval import expreval
def test_expreval():
    e = Node("*", Node("+", leaf(2), leaf(5)),leaf(6))
    assert(expreval (e.left.left) == 2)
    assert(expreval (e.left) == 7)
    assert(expreval (e) == 42)

def test_expreval_1():
    e = Node("+",leaf(2),leaf(3))
    assert(expreval(e) == 5)
