"""
140. Word Break - II
"""

from typing import List

"""
def wordBreak(self, s, wordDict):
    return self.helper(s, wordDict, {})
    
def helper(self, s, wordDict, memo):
    if s in memo: return memo[s]
    if not s: return []
    
    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)
        else:
            resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
            for item in resultOfTheRest:
                item = word + ' ' + item
                res.append(item)
    memo[s] = res
    return res
"""


class Solution:
    def __init__(self):
        self.res = []

    # TOP - DOWN Approach
    def dfs(self, s, path, dp, ind, word_dict):
        if dp[ind + len(s)]:
            if not s:
                self.res.append(path.strip())

            for i in range(1, len(s) + 1):
                if s[:i] in word_dict:
                    self.dfs(s[i:], path + " " + s[:i], dp, ind + i, word_dict)

    def build_possible_word_starts(self, s, word_dict):
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        for i in range(N):
            for j in range(i, N + 1):
                if dp[i] and s[i:j] in word_dict:
                    dp[j] = True
        return dp

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return [""]
        wordDict = set(wordDict)
        dp = self.build_possible_word_starts(s, wordDict)
        self.dfs(s, "", dp, 0, wordDict)
        return self.res

s = Solution()
print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))