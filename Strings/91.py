"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""


def num_decoding(s):
    if s == "":
        return 0
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    for i in range(1, len(s) + 1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if i > 1 and '10' <= s[i-2: i] <= '26':
            dp[i] += dp[i-2]
    return dp[-1]


num_decoding("226")


def num_decoding_constant_variables(s):
    # instead of using DP array, use 2 variables to store the dp[i-1] and dp[i-2] values
    if not s or s[0] == '0':
        return 0
    prev, curr = 1, 1  # prev = s[i-2], curr = s[i-1], initialized to 1
    for i in range(1,len(s)):
        # letter 0 is not allowed, set curr to 0
        if s[i] == '0':
            curr = 0
        # two letters case
        if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
            tmp = curr
            curr += prev  # curr is the sum of curr and prev
            prev = tmp  # old curr
        # one letter case, so no change
        else:
            prev = curr  # no change
    return curr

