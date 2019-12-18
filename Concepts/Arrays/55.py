from enum import Enum

'''

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

Solution:

This is a dynamic programming1 question. Usually, solving and fully understanding a dynamic programming problem is a 4 step process:

Start with the recursive backtracking solution
Optimize by using a memoization table (top-down3 dynamic programming)
Remove the need for recursion (bottom-up dynamic programming)
Apply final tricks to reduce the time / memory complexity
All solutions presented below produce the correct result, but they differ in run time and memory requirements.


'''


def canJumpBackTracking(nums):
    def canJumpFromPosition(pos, nums):
        if pos == len(nums) - 1:
            return True
        maxJump = min(pos + nums[pos], len(nums) - 1)
        for i in range(pos + 1, maxJump + 1):
            if canJumpFromPosition(i, nums):
                return True
        return False

    return canJumpFromPosition(0, nums)


print(canJumpBackTracking([2, 3, 1, 1, 4]))  # should return True
print(canJumpBackTracking([2, 3, 1, 0, 0, 1]))  # should return False

# use memoization to use dp
from enum import Enum


class state(Enum):
    UNKNOWN = 0
    GOOD = 1
    BAD = -1


def canJumpBackTracking_Top_Down(nums):
    memo = [state.UNKNOWN] * (len(nums))

    def canJumpFromPosition_Top_Down(pos, nums):
        if memo[pos] != state.UNKNOWN:
            return memo[pos] == state.GOOD
        maxJump = min(pos + nums[pos], len(nums) - 1)
        for i in range(pos + 1, maxJump + 1):
            if canJumpFromPosition_Top_Down(i, nums):
                memo[pos] = state.GOOD
                return True
        memo[pos] = state.BAD
        return False

    memo[len(nums) -1] = state.GOOD
    return canJumpFromPosition_Top_Down(0, nums)


print(canJumpBackTracking_Top_Down([2, 3, 1, 1, 4]))
print(canJumpBackTracking_Top_Down([2, 3, 1, 0, 0, 1]))
