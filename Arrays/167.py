'''

167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

'''

def twoSum(nums, target):
  # this is usefull when the array is not sorted.
  dic = {}
  for i in range(len(nums)):
    if target-nums[i] in dic:
      return [dic[target-nums[i]] + 1, i + 1]
    dic[nums[i]] = i
    print(dic)
  return [-1, -1]

twoSum([2, 7, 11, 15], 9)
twoSum([2, 7, 9, 11], 100)

'''
Given that array is sorted, so make use of this
'''
def twoSum_twoPointers(nums, target):
  i, j = 0, len(nums) - 1
  while i < j:
    total = nums[i] + nums[j]
    print(total)
    if total == target:
      return [i + 1, j + 1]
    elif total < target:
      i += 1
    else:
      j -= 1
  return [-1, -1]

twoSum_twoPointers([2, 7, 11, 15], 9)