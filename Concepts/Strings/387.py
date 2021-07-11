"""
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


from collections import Counter


def first_uniq_char(s):
    c = Counter(s)
    print(c)
    for index, ch in enumerate(s):
        if c[ch] == 1:
            return index
    return -1


first_uniq_char("leetcode")
first_uniq_char("loveleetcode")
first_uniq_char("dddccdbba")