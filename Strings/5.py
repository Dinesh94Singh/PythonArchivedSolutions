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
