from dataclasses import dataclass
from typing      import Any, Optional

## Binary Trees ################################################################

@dataclass
class Node:
    mark  : Any
    left  : Optional['Node']
    right : Optional['Node']

def leaf(mark : Any) -> Node:
    return Node (mark, None, None)

def tree_str(tree : Optional[Node]) -> str:
    if tree is None:
        return "None"
    else:
        return ("Node("
            + repr(tree.mark) + ", "
            + tree_str (tree.left) + ", "
            + tree_str (tree.right) + ")")

def height(tree : Optional[Node]) -> int:
    if (tree is None):
        return -1
    else:
        return(max(height(tree.left),
                   height(tree.right)) + 1)

def size(tree : Optional[Node]) -> int:
    if (tree is None):
        return 0
    else:
        return(size(tree.left)
             + size(tree.right) + 1)

def postorder(tree : Optional[Node]):
    if tree is None:
        pass
    else:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.mark)

## Search Tree Operations ######################################################

def search(tree : Optional[Node], item : Any) -> bool:
    if tree is None:
        return False
    elif tree.mark == item:
        return True
    elif tree.mark > item:
        return search(tree.left, item)
    else:
        return search(tree.right, item)

def insert(tree : Optional[Node], item : Any) -> Node:
    if tree is None:
        return leaf(item)
    elif tree.mark > item:
        return Node (tree.mark,
                     insert (tree.left, item),
                     tree.right)
    elif tree.mark < item:
        return Node (tree.mark,
                     tree.left,
                     insert(tree.right, item))
    else:
        return tree

def insertall(tree : Optional[Node], lst  : list[Any]) -> Optional[Node]:
    for key in lst:
        tree = insert (tree, key)
    return tree

def insertm(tree : Optional[Node], item : Any) -> Node:
    if tree is None:
        return leaf(item)
    if tree.mark > item:
        tree.left = insertm(tree.left, item)
    elif tree.mark < item:
        tree.right = insertm(tree.right, item)
    return tree

def insertmall(tree : Optional[Node], lst  : list[Any]) -> Optional[Node]:
    for key in lst:
        tree = insertm (tree, key)
    return tree

example: Node = \
    Node('*', Node('*', Node('+', Node(5, None, None),
                                  Node(6, None, None)),
                        Node(3, None, None)),
              Node(2, None, None))
