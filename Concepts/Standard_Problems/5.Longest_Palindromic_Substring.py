"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

# Top Down Soution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def rec_helper(start_idx, end_idx):
            if start_idx > end_idx:
                return 0
            if start_idx == end_idx:
                return 1
            
            if s[start_idx] == s[end_idx]:
                remaining_length = end_idx - start_idx - 2
                
                c = rec_helper(start_idx + 1, end_idx - 1)
                
                if c == remaining_length:
                    return c + 2

            c1 = rec_helper(start_idx + 1, end_idx)
            c2 = rec_helper(start_idx, end_idx - 1)
            
            return max(c1, c2)
        
        return rec_helper(0, len(s) - 1)