"""
I hate binary trees
"""
from tree import Node, leaf
from expr_parser import parse
from typing import Optional
example = Node('+', Node('*', leaf(2),
leaf('x')),
leaf(5))

def is_var(tree: Optional[Node]):
    if isinstance(tree.mark,str):
        return True
    return False

def is_val(tree: Optional[Node]):
    if isinstance(tree.mark,int):
        return True
    return False

def is_op(tree: Optional[Node]):
    if tree.mark == "*" or tree.mark == "+":
        return True
    return False

def is_add(tree: Optional[Node]):
    if tree.mark == "+":
        return True
    return False

def is_mul(tree: Optional[Node]):
    if tree.mark == "*":
        return True
    return False
assert(is_var(leaf('x')))
assert not(is_var(leaf(5)))
assert(is_val(leaf(5)))
assert not(is_val(leaf('x')))
assert(is_op(Node('*', leaf(5), leaf(6))))
assert not(is_op(leaf('x')))
assert(is_op(example))
assert(is_add(example))
assert not(is_mul(example))

def show_node(tree: Optional[Node]):
    if tree.left is None:
        return str(tree.mark)
    if tree.right is None:
        return str(tree.mark)
    return "(" + show_node(tree.left) + " " + str(tree.mark) + " " + show_node(tree.right) + ")"
#print(show_node(example))
assert(show_node(example) == '((2 * x) + 5)')
assert(show_node(leaf('x')) == 'x')
assert(show_node(leaf(2)) == '2')

def show_node_prefix(tree :Optional[Node]):
    if tree.mark is None:
        return str(tree.mark)
    if tree.left is None:
        return str(tree.mark)
    if tree.right is None:
        return str(tree.mark)
    return str(tree.mark) + " " + show_node_prefix(tree.left) + " " + show_node_prefix(tree.right)


#print(show_node_prefix(example))
assert(show_node_prefix(example) == '+ * 2 x 5')
assert(show_node_prefix(parse('1 + 2')) == '+ 1 2')
assert(show_node_prefix(parse('(1 * 2) + (3 * 4)')) == '+ * 1 2 * 3 4')

def opt_times_two(e : Optional[Node]):
    if e.mark == "+":
        if e.left == e.right:
            return parse(str(2) + " " + str("*") + " " + (show_node(e.right)))
        return None
    return None
a = opt_times_two(parse("(5 * 3) + (5 * 3)"))
#print(show_node(a))
assert(opt_times_two(parse('x + x')) == parse('2 * x'))
assert(opt_times_two(parse('(5 * 3) + (5 * 3)')) == parse('2 * (5 * 3)'))
assert(opt_times_two(parse('x + y')) == None)
assert(opt_times_two(parse('x + (x + x)')) == None)
def opt_assoc(e : Optional[Node]):
    if len(show_node(e.left)) == 1:
        if e.mark != e.right.mark:
            return None
        else:
            old_x = e.left.mark
            old_y = e.right.left.mark
            old_z = e.right.right.mark
            e.left = e.right
            e.left.left.mark = old_x
            e.left.right.mark = old_y
            return parse(show_node(e.left) + " " + e.mark + " " + old_z)
    return None

assert(opt_assoc(parse('x * (y * z)')) == parse('(x * y) * z'))
assert(opt_assoc(parse('x + (y + z)')) == parse('(x + y) + z'))
assert(opt_assoc(parse('x + (y * z)')) == None)
assert(opt_assoc(parse('(x + y) + z')) == None)
print(parse("x + (y * z)" ))
def opt_eval(e : Optional[Node]):
    if  is_val(e.left) and is_val(e.right):
        if e.mark == "+":
            result = int(show_node(e.left)) + int(show_node(e.right))
            return parse(str(result))

        if e.mark == "*":
            result = int(show_node(e.left)) * int(show_node(e.right))
            return parse(str(result))
    return None


assert opt_eval(parse('2 * 3')) == parse('6')
assert opt_eval(parse('2 + 3')) == parse('5')
assert opt_eval(parse('2 * x')) == None
assert opt_eval(parse('2 * (3 * 4)')) == None
def apply_op(op:str,l:int,r:int) -> Optional[int]:
    if op == "+":
        return l + r

    if op == "*":
        return l * r
    else:
        return None

assert apply_op('+', 2, 3) == 5
assert apply_op('*', 2, 3) == 6
assert apply_op('x', 2, 3) == None

def opt_any(e : Optional[Node]):
    o = opt_times_two(e)
    if o != None:
        return parse(show_node(o))
    o = opt_assoc(e)
    if o != None:
        return parse(show_node(o))
    o = opt_eval(e)
    if o != None:
        return parse(show_node(o))
    if is_op(e):
        try:
            o = opt_any(e.right)
            if o != None:
                return parse(show_node(e.left) + " " + e.mark + " " + show_node(o))
        except Exception:
            try:
                o = opt_any(e.left)
                if o != None:
                    return parse(show_node(o) + " " + e.mark + " " + show_node(e.right))
            except Exception:
                return None

#print(opt_any(parse("(x + x) + (x + x)")))
#a = (opt_any(parse("(x + x) + (x + x)")))
#print(show_node(a))
#b = opt_any(parse(show_node(a)))
#print(show_node(b))
#print(opt_any(parse("((2 * 2) * x)")))
#print((parse("((2 * 2) * x)")))
assert(opt_any(parse('(x + x) + (x + x)')) == parse('(2 * (x + x))'))
#assert(opt_any(parse('(2 * (x + x))')) == parse('(2 * (2 * x))'))
assert(opt_any(parse('(2 * (2 * x))')) == parse('((2 * 2) * x)'))
assert(opt_any(parse('((2 * 2) * x)')) == parse('(4 * x)'))
assert(opt_any(parse('(4 * x)')) == None)

def opt_all(e : Optional[Node]):
    lst = [e]
    count = 0
    while True:
        try:
            count += 1
            lst.append(opt_any(lst[count - 1]))
        except Exception:
            return lst

#print((opt_all(parse("(x + x) + (x + x)"))))
#print((opt_all(parse("2 * (x + x)"))))
print(parse("2 * (x + x)"))
#assert opt_all(parse('(x + x) + (x + x)')) == [
#parse('(x + x) + (x + x)'),
#parse('(2 * (x + x))'),
#parse('(2 * (2 * x))'),
#parse('((2 * 2) * x)'),
#parse('(4 * x)')
#]

