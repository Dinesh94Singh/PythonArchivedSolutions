"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""

import collections


def longest_substring_two_dist_chars(s: str) -> int:
    unique_chars = collections.defaultdict(int)

    end = 0
    start = 0
    max_length = float('-inf')

    while end < len(s):
        while len(unique_chars) >= 2 and start <= end and s[end] not in unique_chars:
            unique_chars[s[start]] -= 1
            if unique_chars[s[start]] == 0:
                del unique_chars[s[start]]
            start += 1
        unique_chars[s[end]] += 1
        if max_length < (end - start + 1):
            max_length = (end - start + 1)

        end += 1

    if max_length < (end - start):
        max_length = (end - start)

    return max_length


print(longest_substring_two_dist_chars("ccaabbb"))  # 5
print(longest_substring_two_dist_chars("eceba"))  # 3
