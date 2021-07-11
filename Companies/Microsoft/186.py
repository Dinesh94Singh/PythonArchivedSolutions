"""
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""


class Solution:
    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        s = s[::-1]  # reverse the sentence

        start = 0
        end = 0
        while end < len(s):
            if s[end] == ' ':
                reverse(s, start, end-1)
                end += 1
                start = end
            else:
                end += 1
        reverse(s, start, end - 1)  # for last word
        print(s)


s = Solution()
print(s.reverseWords(["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]))
