"""

5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


"""


def longest_palindrome(s):
    def palindrome(string):
        return string == string[::-1]

    n = len(s)
    sub_sequence = ""
    left = 0
    while left < n:
        right = left + 1  # reset the window
        while right <= n:
            substr = s[left:right]
            if palindrome(substr) and len(substr) > len(sub_sequence):
                sub_sequence = substr
            right += 1
        left += 1
    return sub_sequence


longest_palindrome("babad")

def longest_palindrome_expand_center(s):
    def helper(s, l, r):
        while s[l] == s[r] and l < r < len(s):
            l -= 1
            r += 1
        return s[l, r+1]
    left = 0
    right = len(s)
    res = ''
    for i in range(len(s)):
        tmp = helper(s, i, i) # even
        if len(tmp) > len(res):
            res = tmp
        tmp = helper(s, i, i+1) # odd
        if len(tmp) > len(s):
            res = tmp
    return res
