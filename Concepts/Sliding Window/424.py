'''
424. Longest Repeating Character Replacement

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


'''
from collections import Counter
def characterReplacement(s, k):
    window_start = 0
    counts = Counter() # by default if the entry is not found, it is 0
    window_end = 0
    for window_end in range(1, len(s) + 1):
        counts[s[window_end - 1]] += 1
        max_occuring_char = counts.most_common(1)[0][1]
        if window_end - window_start - max_occuring_char > k:
            # chance to reduce the window size
            counts[s[window_start]] -= 1 # one might think, why we r writing in if block, reason is because, at most one char is either getting deleted or added. so it won't be a loop.
            window_start += 1
    print(window_start, '-', window_end)
    return window_end - window_start

characterReplacement('AABABBA', 1)
characterReplacement('ABAB', 2)