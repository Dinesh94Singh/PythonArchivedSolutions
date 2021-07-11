"""

1047. Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.



Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        i = 0

        while i < len(s):
            print(stack, s[i])
            if i == 0 or s[i] != s[i - 1]:
                stack.append(1)
                i += 1
            else:
                prev_count = stack.pop()

                if prev_count + 1 == 2:
                    s = s[:i - 1] + s[i+1: ]
                    i = i - 1
                else:
                    stack.append(prev_count + 1)
                    i += 1
        return s
    
s = Solution()
print(s.removeDuplicates("abbaca"))