'''
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

# def threeSumClosest(self, nums: List[int], target: int) -> int:

def threeSumClosest(nums, target):
  n = len(nums)
  nums.sort()
  result = nums[0] + nums[1] + nums[2]
  for i in range(n-2):
    l = i + 1
    r = n - 1
    while l < r:
      sum = nums[i] + nums[l] + nums[r]
      if sum == target:
        return sum
      if abs(sum - target) < abs(result - target):
        # found closer value
        result = sum
      if sum < target:
        l = l + 1
      elif sum > target:
        r = r - 1
      else:
        return result
  return result

threeSumClosest([-1, 2, 1, -4], 1)

threeSumClosest([-3,-2,-5,3,-4], -1)