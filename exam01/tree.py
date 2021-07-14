from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    mark: str
    left: Optional["Node"]
    right: Optional["Node"]


def layer(n:int,node:Node):
    if node is None:
        return -1
    if n == 0:
        return [node.mark]
    if n == 1:
        return [node.left.mark,node.right.mark]


tree = Node("0",Node("1a",None,Node("2",None,None)),Node("1b",None,None))
print(tree)
print(layer(0,tree))
print(layer(1,tree))
print(layer(2,tree))
