def find_averages_of_subarrays(K, arr):
    windowStart = 0
    windowEnd = 0
    windowSum = 0
    results = []
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K-1:
            avg = windowSum / K
            windowSum -= arr[windowStart]
            windowStart += 1
            results.append(avg)
    return results

find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])