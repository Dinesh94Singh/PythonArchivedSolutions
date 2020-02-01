'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

# def containsDuplicate(self, nums: List[int]) -> bool:
def containsDuplicate(nums):
  nums.sort()
  i = 0
  for j in range(1, len(nums)):
    if nums[j] == nums[i]:
      return True
    else:
      continue
    i = i + 1
    j = j + 1
  return False

containsDuplicate([1, 1, 2, 3, 4, 5])