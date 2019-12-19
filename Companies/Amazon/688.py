"""
688. Knight Probability
"""

"""
    TC - O(N^2* K)
    SC - O(N^2)

"""
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0 for _ in range(N)] for _ in range(N)]  # This is to store results of Kth step (old)
        dp[r][c] = 1  # our starting point

        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for _ in range(k):
            # make k steps
            dp2 = [[0 for _ in range(N)] for _ in range(N)]  # Store results of K-1th Step (latest)
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in directions:
                        if 0 <= r + dr < N and 0 <= c + dc < N:  # if in bounds => make 1/8 moves
                            dp2[r + dr][c + dc] += val / 8.0

            dp = dp2

        return sum(map(sum(dp)))