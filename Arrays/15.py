'''
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Solution:

1. Iterate through every number in nums
2. The number we are iterating is the target and find the other two numbers, like how we did in 1. two sum Problem 
3. Using two pointers on two sum L and R (L -> Left to Right) and ( R -> Right to Left)
4. Sort the array, so we can easily move i around and know how to adjust L and R (Look Cal Total).
5. If number is same as the number before, we have used it as target previously, so simply continue.

Cal Total:
1. If the total is less than 0, move the Left pointer to make it bigger
2. If the total is bigger than 0, move the Right pointer to make it smaller
3. If the total is 0, we have our answer

'''

def threeSum(nums):
  res = []
  nums.sort()
  length = len(nums)
  # We need atleast 2 numbers to find 3 number sum, L = i+1 and R = L - 1 i.e i+1+1
  for i in range(length - 2):
    if nums[i] > 0:
      # if nums[i] is greater than 0, the numbers coming after i would also be greater than 0
      # since L start from i+1, the lower bound itself is positive number, so we would not be able to find the total as 0, from here
      break
    if i > 0 and nums[i] == nums[i-1]:
      # we have already previously visited i-1 and we might have found a pair for it
      # so simply continue
      continue
    L, R = i+1, length -1
    while L < R:
      total = nums[i] + nums[L] + nums[R]
      if total == 0:
        res.append([nums[i], nums[L], nums[R]])
        # Point L and R to next different numbers, so we don't get repeating numbers
        while L < R and nums[L] == nums[L+1]:
          L = L + 1
        while L < R and nums[R] == nums [R-1]:
          R = R - 1
        L = L + 1
        R = R - 1
      elif total < 0:
        L = L + 1
      elif total > 0:
        R = R - 1
    print(res)