"""
Lexicographically smallest string formed by removing at most one character.

Example 1:

Input: "abczd"
Output: "abcd"
"""

def remove_lexographically(s):
    " what is abcedf - should i remove the f yes"
    i = 0
    j = len(s)
    while i < j - 1:
        if s[i] > s[i+1]:
            return s[:i] + s[i+1:]
        i += 1
    return s[: j-1]

print(remove_lexographically("abyczd"))
print(remove_lexographically("abcde"))
