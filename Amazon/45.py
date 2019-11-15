"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

def min_jumps_to_reach_end(nums):
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    cache = []
    for i in range(1, len(nums)):
        for j in range(i, nums[i]):
            next = min(i + j, len(nums) - 1)
            cache[next] = min(cache[next], )
