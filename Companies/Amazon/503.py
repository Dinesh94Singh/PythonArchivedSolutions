"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""

import collections

class Solution:
    def nextGreaterElements(self, nums):
        stack, r = [], [-1] * len(nums)
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                r[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)): # for circular array
            while stack and (nums[stack[-1]] < nums[i]):
                r[stack.pop()] = nums[i]
            if stack == []:
                break
        return r

s = Solution()
# print(s.nextGreaterElements([1, 2, 1]))
# print(s.nextGreaterElements([5, 4, 3, 2, 1]))
# print(s.nextGreaterElements([1, 9, 2, 7, 4, 10, 8]))
print(s.nextGreaterElements([100, 1, 11, 1, 120, 111, 123, 1, -1, -100])) # should be [120,11,120,120,123,123,-1,100,100,100]
