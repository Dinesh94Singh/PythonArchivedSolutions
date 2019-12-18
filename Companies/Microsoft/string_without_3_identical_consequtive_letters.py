"""
Given a string, remove minimum possible letters to return the string which at most 2 identically consequite letters.

Example:
eedaaad -> eedaad (we removed the extra 'a')
"""

from itertools import groupby
def stringWithout3Identical(S):
    ans = ''
    for c, g in groupby(S):
        L = len(list(g))
        ans += c * min(L, 2)
    return ans

S = 'eedaaad'
print(stringWithout3Identical(S))

def stringWithout3Identical_myVariant(s):
    end = 0
    count = 1
    ch = s[end]
    ans = s[0]
    while end < len(s):
        if s[end] == ch:
            count += 1
            if count < 3:
                ans += s[end] #
        else:
            ch = s[end]
            ans += s[end]
            count = 1
        end += 1
    return ans

print(stringWithout3Identical_myVariant('eeedaaadd'))
print(stringWithout3Identical_myVariant('xxtxx'))
print(stringWithout3Identical_myVariant('uuxaaxuu'))
print(stringWithout3Identical_myVariant('eedaaddddd'))
