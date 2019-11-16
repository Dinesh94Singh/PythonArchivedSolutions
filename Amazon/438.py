"""
438: Find all anagrams in a String
"""

from collections import defaultdict


class Solution:
    def findAnagrams(self, s, p):
        p_dict = defaultdict(int)
        s_dict = defaultdict(int)

        for i in range(len(p)):
            p_dict[p[i]] += 1

        l = len(p)
        res = []

        if s_dict == p_dict:
            res.append(0)

        start = 0
        end = l

        while end < len(s) - 1:
            s_dict[s[start]] -= 1
            s_dict[s[end - 1]] += 1

            print(s[start: end + 1], s_dict, end='\t')
            if p_dict == s_dict:
                res.append(end)

            start += 1
            end += 1

        return res


s = Solution()
print(s.findAnagrams("abab", "ab"))
print(s.findAnagrams("baa", "aa"))
print(s.findAnagrams("bpaa", "aa"))
