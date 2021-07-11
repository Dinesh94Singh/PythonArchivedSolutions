"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""

def longest_palindromic_subseq(s):
    def rec_helper(start_idx, end_idx):
        if start_idx > end_idx:
            return 0
        elif start_idx == end_idx:
            return 1
        c = 0
        if s[start_idx] == s[end_idx]:
            c = 2 + rec_helper(start_idx + 1, end_idx - 1)
        
        c1 = rec_helper(start_idx + 1, end_idx)
        c2 = rec_helper(start_idx, end_idx - 1)

        return max(c, max(c1, c2))

    return rec_helper(0, len(s) - 1)

print(longest_palindromic_subseq("bbbab"))
print(longest_palindromic_subseq("cbbd"))