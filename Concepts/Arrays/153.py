'''
153. Find minimum in rotated sorted array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

Solution.
1. Find the index where the rotation happens, if it is 0, then the min element would be a[0] else, traverse till the element where nums[i] > nums[i+1], then i+1 would be the result.
'''
def find_rotation_index(left, right, nums):
  if nums[left] < nums[right]:
    # the array is not rotated.
    return 0
  while left < right:
    pivot = (left + right) // 2
    if nums[pivot] > nums[pivot + 1]:
      return pivot + 1
    else:
      if nums[pivot] < nums[left]:
        right = pivot - 1
      else:
        left = pivot + 1


def findMin(nums):
  idx = find_rotation_index(0, len(nums) - 1, nums)
  if idx == 0:
    return nums[0]
  return nums[idx]
findMin([3,4,5,1,2])
findMin([2, 3, 4, 5, 1])
findMin([0, 1, 2, 3, 4])
findMin([95, 96, 97, 98, 0, 1, 2])