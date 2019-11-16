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

def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    max_length = float('-inf')
    sub_string = ''

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            max_length = 2
            sub_string = s[i: i + 2]

    for window_size in range(3, n + 1):
        for start in range(n - window_size + 1):
            end = start + window_size - 1
            print(s[start: end + 1], s[start] == s[end],  dp[start+1][end-1])
            if s[start] == s[end] and dp[start+1][end-1]:
                dp[start][end] = True

                if max_length < end - start + 1:
                    max_length = window_size
                    sub_string = s[start: end+1]
    return sub_string

# print('longest substring is', longest_palindromic_substring('babad'))
print('longest substring is', longest_palindromic_substring('cbbd'))