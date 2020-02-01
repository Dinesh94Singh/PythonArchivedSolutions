"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

from collections import Counter
def canPermutePalindrome(s):
    c = Counter(s)
    limit = True
    for key in c.keys():
        value = c[key]
        if value % 2 == 0:
            pass
        else:
            if limit:
                limit = False
            else:
                return False
    return True

canPermutePalindrome("code")
canPermutePalindrome("aab")
canPermutePalindrome("carerac")
