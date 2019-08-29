'''
53. Max Sub Array

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Solution:

1. Sum with prev array elements, if only it is less than 0. At each value check with max_sum.
2. By end you should get the max_sum

[-2, 1, -3, 4, -1, 2, 1, -5, 4]
[-2, 1, -2, 4, -1, 2, 1, -5, 4]
[-2, 1, -2, 4, -1, 2, 1, -5, 4]
[-2, 1, -2, 4, 3, 2, 1, -5, 4]
[-2, 1, -2, 4, 3, 5, 1, -5, 4]
[-2, 1, -2, 4, 3, 5, 6, -5, 4]
[-2, 1, -2, 4, 3, 5, 6, 1, 4]
[-2, 1, -2, 4, 3, 5, 6, 1, 5]
'''

def maxSubArray(nums):
  n = len(nums)
  max_sum = nums[0]
  for i in range(1, n):
    if nums[i-1] > 0:
      nums[i] += nums[i-1]
    max_sum = max(nums[i], max_sum)
    print(nums)
  return max_sum

def maxSubArray_greedy(nums):
  n = len(nums)
  curr_sum = max_sum = nums[0]
  print(curr_sum)
  for i in range(1, n):
      curr_sum = max(nums[i], curr_sum + nums[i])
      print(curr_sum)
      max_sum = max(max_sum, curr_sum)
      
  return max_sum

maxSubArray_greedy([-2, 1, -3, 4, -1,  2, 1, -5, 4])