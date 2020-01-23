"""
291. Word Pattern - II
"""

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty
substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
Notes:
You may assume both pattern and str contains only lowercase letters.
"""


class Solution:
    def word_pattern(self, input, pattern):
        """
            Brute Force:
                1. Consider each char as word and create a map from pattern
                    input - redblueredblue
                    pattern - abab

                    a - r              .....  a - red
                    b - e              .....  b - blue
                    a - d (X fails)
        """
        def is_match(s, s_index, pattern, p_index, dic):
            if s_index == len(s) and p_index == len(pattern):
                return True
            if s_index == len(s) or p_index == len(pattern):
                return False

            ch = pattern[p_index]
            print(dic)
            if ch in dic:
                val = dic[ch]

                if not s.startswith(val, s_index):
                    return False

                return is_match(s, s_index + len(val), pattern, p_index + 1, dic)
            else:
                for i in range(s_index, len(s)):
                    t = s[s_index: i + 1]
                    dic[ch] = t

                    if is_match(s, i + 1, pattern, p_index + 1, dic):
                        return True

                    del dic[ch]

                return False

        dic = {}
        return is_match(input, 0, pattern, 0, dic)


sol = Solution()

pat = "aabb"
string = "xyzabcxzyabc"


pat2 = "aaaa"
string2 = "asdasdasdasd"

print(sol.word_pattern(string2, pat2));
