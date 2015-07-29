"""
"+ + 1 2 3"

expr is a polish notation list
"""


def solve(expr):
    """Solve the polish notation expression in the list `expr` using a stack.
    """
    operands = []
    # Scan the given prefix expression from right to left
    for op in reversed(expr):
        if op == "+":
            operands.append(operands.pop() + operands.pop())
        elif op == "-":
            operands.append(operands.pop() - operands.pop())
        else:
            operands.append(float(op))
    return operands.pop()


assert solve("+ + 1 2 3".split()) == 6
assert solve("+ 10 5".split()) == 15
assert solve("- 15 - 7 + 1 1".split()) == 10
