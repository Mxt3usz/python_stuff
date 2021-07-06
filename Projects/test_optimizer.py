from optimizer import opt_all
from expr_parser import parse

def test_optimizer():
    assert opt_all(parse('(x + x) + (x + x)')) == [
    parse('(x + x) + (x + x)'),
    parse('(2 * (x + x))'),
    parse('(2 * (2 * x))'),
    parse('((2 * 2) * x)'),
    parse('(4 * x)')
    ]
