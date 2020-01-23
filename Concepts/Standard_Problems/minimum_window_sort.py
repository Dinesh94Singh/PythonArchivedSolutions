"""
Minimum Window Sort (medium)
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted
Example 4:
"""


def shortest_window_sort(arr):
    p1 = -1
    p2 = -1
    i = 1
    while i < len(arr) - 1:
        if arr[i-1] > arr[i]:
            p1 = i - 1
            break
        i += 1
    if i == len(arr) - 1:
        return 0
    j = len(arr) - 2
    while j > 0:
        if arr[j] > arr[j+1]:
            p2 = j + 1
            break
        j -= 1
    while p1 > 0 and arr[p1 - 1] > min(arr[i: j+1]):
        p1 = p1 - 1
    while p2 < len(arr) - 1 and arr[p2 + 1] < max(arr[i: j+1]):
        p2 = p2 + 1
    return p2 - p1 + 1


shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12])
shortest_window_sort([1, 2, 3])
shortest_window_sort([1, 3, 2, 0, -1, 7, 10])
