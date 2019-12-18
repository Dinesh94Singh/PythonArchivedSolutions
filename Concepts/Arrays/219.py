"""
219. Contains Duplicates 2
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""


def contains_nearby_duplicate(nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            print(i)
            return True
        dic[v] = i
    return False


contains_nearby_duplicate([1, 2, 3, 1], 3)
contains_nearby_duplicate([1, 0, 1, 1], 1)
contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)

from collections import defaultdict


def contains_nearby(nums, k):
    dic = defaultdict(list)
    for i, v in enumerate(nums):
        dic[v].append(i + 1)
    print(dic)
    for values in dic.values():
        x = values
        for idx in range(1, len(x)):
            print(x[idx], x[idx - 1])
            if x[idx] - x[idx - 1] <= k:
                return True
    return False


contains_nearby([1, 0, 1, 1], 1)
contains_nearby([1, 2, 3, 1], 3)
contains_nearby([1, 2, 3, 1, 2, 3], 2)
