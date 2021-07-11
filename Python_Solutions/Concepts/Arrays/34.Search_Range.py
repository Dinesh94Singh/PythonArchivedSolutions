"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target val.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


def search_range(nums, target):
    def binary_search(left, right, is_left):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target or (is_left and nums[mid] == target):
                right = mid
            else:
                left = mid + 1
        return left

    lo = binary_search(0, len(nums), True)
    hi = binary_search(0, len(nums), False)
    return [lo, hi]


nums = [5, 7, 7, 8, 8, 10]
search_range(nums, 8)
