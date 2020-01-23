"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

def minDistance(word1: str, word2: str) -> int:
    def rec_helper(idx1, idx2, cache):
        if idx1 == len(word1):
            return len(word2) - idx2
        if idx2 == len(word2):
            return len(word1) - idx1
        
        if cache[idx1][idx2] != float('-inf'):
            return cache[idx1][idx2]

        if word1[idx1] == word2[idx2]:
            # the chars are same, no need to replace here
            return rec_helper(idx1 + 1, idx2 + 1, cache)
        
        c1 = 1 + rec_helper(idx1 + 1, idx2, cache)
        c2 = 1 + rec_helper(idx1, idx2 + 1, cache)
        c3 = 1 + rec_helper(idx1 + 1, idx2 + 1, cache)
        
        cache[idx1][idx2] = min(c1, min(c2, c3))
        return cache[idx1][idx2]

    cache = [[float('-inf') for _ in range(len(word2))] for _ in range(len(word1))]
    return rec_helper(0, 0, cache)