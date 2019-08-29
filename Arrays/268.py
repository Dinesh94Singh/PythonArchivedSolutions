'''
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

# def missingNumber(self, nums: List[int]) -> int:

'''

We cannot use algorithm from #448 because the input range is not 1<=a[i]<=n

# def missingNumber(nums):
#   for i in range(len(nums)):
#     idx = abs(nums[i]) - 1
#     nums[idx] = -abs(nums[idx])
#   print(nums)

#   values = [i+1 for i in range(len(nums) - 1) if nums[i] >= 0]
#   return values[0]


# missingNumber([9,6,4,2,3,5,7,0,1])

# missingNumber([0])

'''

def missingNumber_guassFormulae(nums):
  expected_sum = (len(nums) * len(nums)+1)//2
  total_sum = sum(nums)
  return expected_sum - total_sum

def missingNumber_sort(nums):
  nums.sort()
  if nums[-1] != len(nums):
    return len(nums)
  # Ensure that 0 is at the first index
  elif nums[0] != 0:
    return 0
  print(nums)
  for i in range(len(nums)):
    if nums[i] != i:
      return i
missingNumber_sort([9, 6, 4, 2, 3, 5, 7, 0, 1])
missingNumber_sort([0])

def missingNumber_bitManipulation(nums):
  missing = len(nums)
  for i, num in enumerate(nums):
    missing ^= i ^ num
  return missing