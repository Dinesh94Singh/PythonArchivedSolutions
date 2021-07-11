def longestPalindrome_dynamicProgramming(s: str) -> int:
    # dp solution

    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for window_size in range(2, n + 1):
        print('for window_size ', window_size - 1)
        for i in range(len(dp)):
            print(dp[i])

        for start in range(n - window_size + 1):
            end = start + window_size - 1

            if s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1] + 2
            else:
                dp[start][end] = max(dp[start][end - 1], dp[start + 1][end])

    return dp[0][n - 1]

x = []
x.clear()
# print(longestPalindrome_dynamicProgramming("babad"))
print(longestPalindrome_dynamicProgramming("bxbabyb"))