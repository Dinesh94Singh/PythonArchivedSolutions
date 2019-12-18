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


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search_iterative(left, right, target):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        def get_rotated_index(left, right):
            if nums[left] < nums[right]:
                return 0  # its sorted
            while left < right:
                mid = (left + right) // 2

                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1

        n = len(nums)

        if n == 0:
            return -1

        if n == 1:
            return 0 if nums[0] == target else -1

        rotated_index = get_rotated_index(0, n - 1)

        if nums[rotated_index] == target:
            return rotated_index

        if rotated_index == 0:
            return binary_search_iterative(0, n - 1, target)
        else:
            if target < nums[0]:
                # search on the right side
                return binary_search_iterative(rotated_index, n - 1, target)
            # search on the left side
            return binary_search_iterative(0, rotated_index, target)


s = Solution()
print(s.search([3, 1], 3))
