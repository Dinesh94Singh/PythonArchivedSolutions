"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    def isMatch(self, s: str, pattern: str) -> bool:
        if not pattern:
            return s == ''

        first_match = s != '' and (pattern[0] == s[0] or pattern[0] == '.')

        # check if pattern_idx + 2 holds '*' => we have 2 options here
        # 1st option - don't use first_char => isMatch(s, pat_idx + 2)
        # 2nd option = use first char multiple times => first_match and self.isMatch()
        # else - check if first_match and move s_idx + 1, pat_idx + 1

        if len(pattern) >= 2 and pattern[1] == '*':
            if first_match and self.isMatch(s[1:], pattern):
                # use the first_char, multiple times
                return True
            elif self.isMatch(s, pattern[2:]):
                # ignore the * and move forward
                return True
            else:
                return False
        else:
            return first_match and self.isMatch(s[1:], pattern[1:])


s = Solution()
print(s.isMatch("mississippi", "mi.s.*pi"))
print(s.isMatch("aaa", "a*a"))


class My_Solution:
    def isMatch(self, s: str, pattern: str) -> bool:
        def rec_helper(string_idx, pattern_idx):
            nonlocal s, pattern
            if pattern_idx == len(pattern):
                return string_idx == len(s)

            first_match = False

            if string_idx != len(s):
                first_match = pattern[pattern_idx] == s[string_idx] or pattern[pattern_idx] == '.'

            if pattern_idx < len(pattern) - 1 and pattern[pattern_idx + 1] == '*':
                # the next element is '*' -> a* or .*
                if first_match and rec_helper(string_idx + 1, pattern_idx):
                    return True
                elif rec_helper(string_idx, pattern_idx + 2):
                    # skip the element 0 occurences of a
                    return True
                else:
                    return False
            else:
                return first_match and rec_helper(string_idx + 1, pattern_idx + 1)

        return rec_helper(0, 0)


s = My_Solution()
print(s.isMatch("aaa", "a*a"))
