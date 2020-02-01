"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


def word_break_brute_force(s, word_dict):
    def back_track(remaining):
        if remaining == '':
            return True
        for i in range(len(remaining)):
            # in the rest of the remaining stuff
            if remaining[: i + 1] in word_dict:
                if back_track(remaining[i + 1:]):
                    return True
        return False

    return back_track(s)


def word_break_memoization(s, word_dict):
    def back_track_memo(remaining):
        print(memo)
        if remaining == '':
            return True
        if memo.get(remaining, False):
            print('memorizing')
            return memo.get(remaining)  # it could either be True or False
        for i in range(len(remaining)):
            # in the rest of the remaining stuff
            if remaining[: i + 1] in word_dict and back_track_memo(remaining[i + 1:]):
                memo[remaining[i:]] = True
                return True
        memo[remaining] = False
        return False

    memo = {}
    back_track_memo(s)
    print(memo)


def word_break_memoization(s, word_dict):
    def back_track_memo(remaining):
        print(remaining)
        print(memo)
        if remaining == '':
            return True
        if remaining in memo:
            print('memorizing')
            return memo.get(remaining)  # it could either be True or False
        for i in range(len(remaining)):
            # in the rest of the remaining stuff
            if remaining[: i + 1] in word_dict and back_track_memo(remaining[i + 1:]):
                memo[remaining[i + 1:]] = True
                return True
        memo[remaining] = False
        return False

    memo = {}
    print(memo)
    return back_track_memo(s)


def word_break_dp(s, word_dict):
    dp = [False for i in range(len(s) + 2)]
    dp[0] = True
    for length in range(1, len(s)):
        for i in range(length):
            if dp[i] and s[i: length+1] in word_dict:
                dp[length] = True
                break
    print(dp)
    return dp[len(s)]


# word_break_brute_force('applepenapple', ['apple', 'pen'])
word_break_memoization('applepenapple', ['apple', 'pen'])
word_break_memoization('catsandogs', ["cats", "dog", "sand", "and", "cat"])
word_break_dp('catsandogs', ["cats", "dog", "sand", "and", "cat"])
word_break_memoization('catsandogs', ["cats", "dogs", "sand", "and", "cat", "an"])
word_break_dp('catsandogs', ["cats", "dogs", "sand", "and", "cat", "an"])
word_break_dp('applepenapple', ['apple', 'pen'])
word_break_dp('code', ['c', 'od', 'e', 'x'])
