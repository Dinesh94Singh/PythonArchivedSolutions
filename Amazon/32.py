"""
32. Longest Valid Parenthesis
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


def longestValidParentheses(s: str) -> int:
    #  stack implementation and finding the len when it fails??
    stack = []
    end = 0
    ans = float('-inf')
    value = 0
    while end < len(s):
        if s[end] == '(' or s[end] == '[' or s[end] == '{':
            stack.append(s[end])
        elif len(stack) > 0 and ((stack[-1] == '(' and s[end] == ')') or (stack[-1] == '[' and s[end] == ']')
                                 or (stack[-1] == '{' and s[end] == '}')):
            value += 2
            stack.pop()
        else:
            # it is an error
            ans = max(ans, value)
            value = 0
            stack.clear()
        end += 1
    ans = max(ans, value)
    return ans













# print(longestValidParentheses("(()"))
# print(longestValidParentheses(")()())"))
# print(longestValidParentheses("({[])}"))
# print(longestValidParentheses('(){}[]'))
print(longestValidParentheses('[([]{{{})}]'))