"""
154. Find Minimum in Rotated Sorted Array II
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""



'''
class Solution(object):
def findMin(self, nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi -lo) / 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo] 
    
Find Minimum in Rotated Sorted Array II----contain duplicates----O(logN)~O(N)

class Solution(object):
def findMin(self, nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi -lo) / 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid if nums[hi] != nums[mid] else hi - 1
    return nums[lo]
'''
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotated = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                rotated = True
                # if there is fall - that is where the rotation happened
                break

        rotated_idx = i

        if rotated_idx == len(nums) - 2 and not rotated:
            return nums[0]
        else:
            return nums[rotated_idx + 1]

s = Solution()
print(s.findMin([1, 3, 5]))

print(s.findMin([2,2,2,0,1]))

print(s.findMin([4,5,6,7,0,1,2]))

print(s.findMin([0,1,2,3,4]))

print(s.findMin([3, 1]))