"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

# TIME LIMIT EXCEEDED

def canJump(nums) -> bool:
    dp = [False for _ in range(len(nums))]
    dp[0] = True
    for i in range(1, len(nums)):
        for j in range(i):
            if dp[i] is False and j + nums[j] >= i and dp[j] is True:
                dp[i] = True
    return dp[-1]


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
