"""

14. Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.


Read - https://leetcode.com/articles/longest-common-prefix/
"""


def longest_common_prefix(strs):
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    prefix = strs[0]
    for i in range(0, len(strs)):
        # iterate through all the given strings
        window_start = 0
        window_end = 0
        s1_len = len(prefix)
        s2_len = len(strs[i])
        min_len = min(s1_len, s2_len)
        while window_end < min_len:
            if prefix[window_end] == strs[i][window_end]:
                # move the window
                window_end += 1
            else:
                break
        prefix = prefix[window_start: window_end] if s1_len < s2_len else strs[i][window_start: window_end]
        print(prefix, ' at step ', i)
    return prefix

longest_common_prefix(["flower","flower","flight"])
longest_common_prefix(["dog","racecar","car"])