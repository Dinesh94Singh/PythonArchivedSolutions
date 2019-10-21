"""
Problem Statement
Given an array with positive numbers and a target number,
find all of its subarrays (contiguous set of elements) whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
Explanation: There are seven subarrays whose product is less than the target.

"""
from collections import deque


def find_sub_arrays(arr, target):
    result = []
    prod = 1
    left = 0
    for right in range(len(arr)):
        prod *= arr[right]
        while prod > target and left < len(arr):
            prod /= arr[left]
            left += 1
        temp_list = deque()
        print('left is ', left, 'right is ', right)
        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
        print(result)
    return result


find_sub_arrays([2, 5, 3, 10], 30)
