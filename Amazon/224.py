"""
224. Basic Calculator

1. Given a valid input
2. Supported operations +, -, (, ), space
"""


class Solution:

    def evaluate_expr(self, stack):

        res = stack.pop() if stack else 0

        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s: str) -> int:

        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():

                # Forming the operand - in reverse order. # characters could be 2 ... n digit length digits
                operand = (10**n * int(ch)) + operand
                n += 1

            elif ch != " ": # if space do nothing
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand) # append values like 12, 24 (2 ... n length digits)
                    n, operand = 0, 0 # get ready for next operation

                if ch == '(':
                    res = self.evaluate_expr(stack)
                    stack.pop()

                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)

                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)  # + , - , ) etc

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return self.evaluate_expr(stack)

s = Solution()
print(s.calculate("1 + 2 - 3"))
print(s.calculate("1 + 2 - 3"))
print(s.calculate("1 + (2 - 3)"))
print(s.calculate("1 + (2) - 3"))
print(s.calculate("12 + ((12 - 10) + 13)"))

