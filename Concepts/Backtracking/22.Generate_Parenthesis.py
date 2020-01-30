"""

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


"""


def generate_parentheses(n):
    def generate(A=[]):
        if A is None:
            A = []
        if len(A) == 2 * n:
            if valid(A):
                ans.append("".join(A))
        else:
            print(A)
            A.append('(')
            generate(A)
            print(A)
            A.pop()
            A.append(')')
            print(A)
            generate(A)
            A.pop()
            print(A)

    def valid(A):
        balance = 0
        for each_char in A:
            if each_char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    ans = []
    generate()
    print(ans)
    print(count, ' is the count')


generate_parentheses(3)


def generate_parentheses_back_tracking(n):
    ans = []

    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            ans.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack()
    return ans


generate_parentheses_back_tracking(3)
