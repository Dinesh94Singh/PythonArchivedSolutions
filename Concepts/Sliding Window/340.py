"""

340. Longest Substring with K Distinct Chars

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""


def longest_substring_with_k_distinct(s, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

import collections

def retry(s, k):
    def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:

        start = 0
        end = 0

        hm = collections.defaultdict(int)
        ans = float('-inf')

        while end < len(s):
            hm[s[end]] += 1
            while start <= end and len(hm) > k:
                hm[s[start]] -= 1

                if hm[s[start]] == 0:
                    del hm[s[start]]

                start += 1
            ans = max(ans, end - start + 1)
            end += 1

        return ans

    print(lengthOfLongestSubstringKDistinct(s, k))

retry('ecaba', 2)