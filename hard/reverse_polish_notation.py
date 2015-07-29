"""
Using the Python language, have the function ReversePolishNotation(str) read str which will be an arithmetic expression composed of only integers and the operators: +,-,* and / and the input expression will be in postfix notation (Reverse Polish notation), an example: (1 + 2) * 3 would be
1 2 + 3 * in postfix notation. Your program should determine the answer for the given postfix expression. For example: if str is 2 12 + 7 / then your program should output 2.

"""


def ReversePolishNotation(expression):
    stack = []
    for s in expression.split():
        if s not in "+-*/":
            stack.append(float(s))
            continue
        s1, s2 = stack.pop(), stack.pop()
        if s == "+":
            stack.append(s1 + s2)
        elif s == "-":
            stack.append(s2 - s1)
        elif s == "*":
            stack.append(s1 * s2)
        elif s == "/":
            stack.append(s2 / s1)
    return int(stack.pop())


assert ReversePolishNotation("1 1 + 1 + 1 +") == 4
assert ReversePolishNotation("4 5 + 2 1 + *") == 27
assert ReversePolishNotation("2 12 + 7 /") == 2
