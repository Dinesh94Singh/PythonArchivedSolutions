"""
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total
number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.



Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
"""


class Solution:
    def mergeStones_recursive_without_memo(self, stones, k):
        def recursive_solution(stones, total_so_far):
            n = len(stones)

            for i in range(n - k + 1):
                start = i
                end = i + k

                if len(stones) == k:
                    self.ans.append(total_so_far + sum(stones))

                recursive_solution(stones[: start] + [sum(stones[start: end])] + stones[end:],
                                   total_so_far + sum(stones[start: end]))

        if len(stones) == 1:
            return 0
        self.ans = []
        recursive_solution(stones, 0)

        return min(self.ans) if len(self.ans) > 0 else -1

    def mergeStones_recursive_with_memo(self, stones, k):
        pass

    def mergeStones_recursive_with_dp(self, s, K):
        N = len(s)
        if (N - 1) % (K - 1): return -1
        preS = [0] * (N + 1)
        for i in range(1, N + 1):
            preS[i] = s[i - 1] + preS[i - 1]
        M = [[float('inf')] * N for _ in range(N)]

        def dp(i, j):
            if M[i][j] == float('inf'):
                if j - i + 1 < K:
                    M[i][j] = 0
                else:
                    M[i][j] = min(dp(i, k) + dp(k + 1, j) for k in range(i, j, K - 1))
                    if (j - i) % (K - 1) == 0:
                        M[i][j] += preS[j + 1] - preS[i]
            return M[i][j]

        return dp(0, N - 1)


cdsfds






s = Solution()
print(s.mergeStones([3, 2, 4, 1], 3))
print(s.mergeStones([3, 2, 4, 1], 2))
print(s.mergeStones([3, 5, 1, 2, 6], 3))
print(s.mergeStones([69, 39, 79, 78, 16, 6, 36, 97, 79, 27, 14, 31, 4], 2))
