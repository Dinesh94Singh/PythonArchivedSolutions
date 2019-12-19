"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

"""
Prefix - Polish Notation
Postfix - Reverse Polish Notation
"""

def evalExpr(tokens):
    stack = []

    for i in range(len(tokens)):
        print(stack)
        if tokens[i].isdigit():
            stack.append(int(tokens[i]))
        else:
            ch = tokens[i]
            x = stack.pop()
            y = stack.pop()
            if ch == "+":
                stack.append(x + y)
            elif ch == '-':
                stack.append(y - x)
            elif ch == '*':
                stack.append(x * y)
            elif ch == '/':
                stack.append(int(y/x))

    print(stack[0])
    
# evalExpr(["4", "13", "5", "/", "+"])
evalExpr(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])