# TIME LIMIT EXCEEDED

class Solution:
    def jump(self, nums):
        dp = [float('inf') for _ in range(len(nums))]
        jump_from = [float('inf') for _ in range(len(nums))]

        dp[0] = 0
        jump_from[0] = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if j + nums[j] >= i:
                    #  from j -> i can reach i by making nums[j] steps
                    if dp[i] > dp[j] + 1:
                        dp[i] = dp[j] + 1
                        jump_from[i] = j
        return dp[-1]


s = Solution()

print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 1, 1, 2, 4, 2, 0, 1, 1]))
