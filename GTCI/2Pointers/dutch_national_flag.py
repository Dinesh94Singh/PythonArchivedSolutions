"""
Given an array containing 0s, 1s and 2s, sort the array in-place.
You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
If you would count, you could simply create a new array
"""

# Brute Force solution is to perform a HeapSort algorithm - using heapq and heapify

# 2 pointers intuition - low and high points to first and last. Move all 0's after low and all 2's after high.


def dutch_flag_sort(arr):
    # elements < low are 0
    # elements > high are 2
    # elements >= low < 1 are 1
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
    return arr


dutch_flag_sort([1, 0, 2, 1, 0])
