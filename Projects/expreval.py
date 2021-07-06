from tree import Node, leaf
from expr_parser import parse
import pytest

def expreval(tree):
    if tree.mark == '+':
        return expreval(tree.left) + expreval(tree.right)
    elif tree.mark == '-':
        return expreval(tree.left)-expreval(tree.right)
    elif tree.mark == '*':
        return expreval(tree.left)*expreval(tree.right)
    elif tree.mark == '/':
        return expreval(tree.left)//expreval(tree.right)
    else:
        return tree.mark

e = Node('+', Node('+', leaf(2), leaf(5)), leaf(6))
#print(expreval(e.left))
print(expreval(e))
#f = Node("-", leaf(42), leaf(2))
#print(f)

