'''
20. Valid Paranthesis

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

def isValid(s):
  stack = []
  if len(s) == 0:
    return True
  if len(s) == 1:
    return False
  for each in s:
    print(stack)
    if each == '(' or each == '[' or each == '{':
      stack.append(each)
    else:
      top = stack[-1] if len(stack) > 0 else ''
      if each == ')' and top == '(' or each == ']' and top == '[' or each == '}' and top == '{':
        stack.pop()
      else:
        return False
  return True if len(stack) == 0 else False