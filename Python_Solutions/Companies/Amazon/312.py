"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

"""
for (int len = 1; len <= nums.length; len++) {
            for (int i = 0; i <= nums.length - len; i++) {
                int j = i + len - 1;
                for (int k = i; k <= j; k++) {
                    //leftValue/rightValue is initially 1. If there is element on
                    // left/right of k then left/right value will take that value.
                    int leftValue = 1;
                    int rightValue = 1;
                    if (i != 0) {
                        leftValue = nums[i-1];
                    }
                    if (j != nums.length -1) {
                        rightValue = nums[j+1];
                    }

                    //before is initially 0. If k is i then before will
                    //stay 0 otherwise it gets value T[i][k-1]
                    //after is similarly 0 initially. if k is j then after will
                    //stay 0 other will get value T[k+1][j]
                    int before = 0;
                    int after = 0;
                    if (i != k) {
                        before = T[i][k-1];
                    }
                    if (j != k) {
                        after = T[k+1][j];
                    }
                    T[i][j] = Math.max(leftValue * nums[k] * rightValue + before + after,
                            T[i][j]);
                }
            }
        }
        return T[0][nums.length - 1];

"""


class Solution:
    def maxCoins(self, nums):
        dp = [[0 for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]

        # add boundaries as 0's

        # since we added 0's as boundaries, the actual index would be from 1
        for l in range(1, len(nums) + 1):
            for start in range(0, len(nums) - l + 1):
                end = start + l - 1
                for k in range(start, end + 1):
                    # check what is the max coins goined by popping the balloon k at the end
                    # initially declare the fields as 1, so that when we multiply, we get a res => left * i * right
                    left_value = 1
                    right_value = 1

                    if start != 0:  # if start == 0, the left_value would be 1
                        left_value = nums[start - 1]

                    if end != len(nums) - 1:
                        right_value = nums[end + 1]

                    # if popping the element in between the window instead of extreme ends before and after would have v
                    before, after = 0, 0
                    if start != k:
                        before = dp[start][k - 1]
                    if end != k:
                        after = dp[k + 1][end]

                    dp[start][end] = max(left_value * nums[k] * right_value + before + after, dp[start][end])

        print(dp)
        return dp[0][-2]


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
