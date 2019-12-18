"""
227. Basic Calculator - 2

1. Given (only positive integers)
2. Should support +, -, *, /, space

/ - floor


Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5

"""
class Solution(object):
    def calculate(self, s):
        """
        Time    O(2n)
        Space   O(n) the stack
        152 ms, faster than 51.65%
        """
        stack = []
        sign = '+' # temp
        num = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10+int(c)
            if i + 1 == len(s) or (c == '+' or c == '-' or c == '*' or c == '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = c
                num = 0
        # O(n) as we iterate the stack to sum
        return sum(stack)

    def calculation_retry(self, s):
        stack = []
        sign = '+' # holds lower precedence value

        operand = 0

        for each_ch_index in range(len(s)):
            ch = s[each_ch_index]
            if ch.isdigit():
                # reverse order => (10**n * int(ch)) + operand => 10^0 * 3 + 10^1 * 0 + 10^2 * 2
                #  102 => 1*10 => 10+0 => 10*10 => 100 + 2 => 102
                operand = operand*10 + int(ch)
            if each_ch_index + 1 == len(s) or (ch == '+' or ch == '-' or ch == '*' or ch == '/'):
                if sign == '+':
                    stack.append(operand)
                elif sign == '-':
                    stack.append(-operand)
                elif sign == '*':
                    x = stack.pop()
                    prod = x * operand
                    stack.append(prod)
                elif sign == "/":
                    x = stack.pop()
                    div = x // operand
                    stack.append(div)
                sign = ch
                operand = 0
        return sum(stack)


s = Solution()
s.calculate("3+2*2") # first 2*2 need to be evaluated
s.calculate("2*2+4") # first 2*2 need to be evaluated
