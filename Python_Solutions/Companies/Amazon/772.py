"""
Basic Calculator - 3

1. +, -, *, /, (, ), space allowed


Ideology:
1.
"""

class Solution(object):

    def calculate(self, s):
        """
        Time    O(n)
        Space   O(n)
        80 ms, faster than 22.22%
        """
        s = s + "$"

        def helper(stack, i):
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                if c.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                elif c == '(':
                    num, i = helper([], i + 1)
                else:
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack.append(stack.pop() * num)
                    if sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stack), i
                    sign = c
            return sum(stack)

        return helper([], 0)
