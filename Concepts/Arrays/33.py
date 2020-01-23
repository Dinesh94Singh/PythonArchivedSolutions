"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


Thought Process:

1. Log n should be the time complexity - possibly binary search. The array is sorted, but we just don't know, where it got rotated.
2. To find where it got rotated, with the middle of the given array, find the smallest element from there using binary search
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_rotated_index(nums):
            start_idx = 0
            end_idx = len(nums) - 1
            while start_idx <= end_idx:
                mid = (start_idx + end_idx) // 2
                
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[start_idx]:
                        end_idx = mid - 1
                    else:
                        start_idx = mid + 1
            
            return -1
    
        def binary_search(start_idx, end_idx, target):
            while start_idx <= end_idx:
                mid = (start_idx + end_idx) // 2
                
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    start_idx = mid + 1
                else:
                    end_idx = mid - 1
            return -1
        
        
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        if nums[0] > nums[-1]:
            rotated_index = find_rotated_index(nums)
        else:
            rotated_index = 0
            
        if nums[rotated_index] == target:
            return rotated_index

        if rotated_index == 0:
            return binary_search(0, len(nums) - 1, target)
        if target < nums[0]:
            return binary_search(rotated_index, len(nums) - 1, target)
        return binary_search(0, rotated_index, target)

s = Solution()
# print(s.search([1, 3], 3))
print(s.search([5, 1, 3], 1))