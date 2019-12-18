"""

125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""

import string


def valid_palindrome(s):
    exclude = set(string.punctuation)
    s = ''.join(ch.lower() for ch in s if ch not in exclude and ch != " ")
    print(s)
    if s[::-1] == s:
        return True
    return False


def valid_palindrome_2_pointer(self, s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():  # just skip if we encounter punctuations
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


valid_palindrome("A man, a plan, a canal: Panama")
valid_palindrome_2_pointer("A man, a plan, a canal: Panama")
