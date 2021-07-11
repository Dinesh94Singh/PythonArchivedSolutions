"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

"""

# def minWindow(self, s: str, t: str) -> str:
from collections import Counter


def min_window(s, t):
    window_start = 0
    window_end = 0
    min_length = (float('inf'), 0, 0)  # store the indexes to return the substring
    t_chars = Counter(t)
    required = len(t_chars)
    window_counts = dict()
    formed = 0
    # if the character is found then return 1
    while window_end < len(s):
        char = s[window_end]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in t_chars and window_counts[char] == t_chars[char]:
            formed += 1
        while window_start <= window_end and formed == required:
            character = s[window_start]
            if window_end - window_start + 1 < min_length[0]:
                min_length = (window_end - window_start + 1, window_start, window_end)
            window_counts[character] -= 1
            if character in t_chars and window_counts[character] < t_chars[character]:
                formed -= 1  # by removing the char, we lost the require char.
            window_start += 1
        window_end += 1
    return "" if min_length[0] == float('inf') else s[min_length[1]: min_length[2] + 1]


min_window("ADOBECODEBANC", 'ABC')


