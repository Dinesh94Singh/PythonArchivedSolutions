"""

647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same
characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""


def sub_string_palindrome(substring):
    if substring[::-1] == substring:
        return True
    return False


def count_sub_strings(s):
    left = 0
    ans = []
    n = len(s)
    while left < n:
        right = left
        while right < n:
            print(s[left: right + 1])
            if sub_string_palindrome(s[left: right + 1]):
                ans.append(s[left: right + 1])
            right += 1
        left += 1
    return len(ans)


count_sub_strings("aaa")
count_sub_strings("abc")


def count_sub_string_expand_center(S):
    N = len(S)
    ans = 0
    for center in range(2 * N - 1):
        left = int(center / 2)
        right = left + int(center % 2)
        while left >= 0 and right < N and S[left] == S[right]:
            print('left and right are - ', (left, right))
            ans += 1
            left -= 1
            right += 1
    return ans


count_sub_string_expand_center("ababa")
