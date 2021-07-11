def max_sum_subarray(k, arr):
    windowStart = 0
    windowEnd = 0
    windowSum = 0
    maximum = float('-inf')
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            maximum = max(maximum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maximum

max_sum_subarray(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
max_sum_subarray(2, [2, 3, 4, 1, 5])
