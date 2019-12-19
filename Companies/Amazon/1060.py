"""
1060. Missing element in sorted Array
"""
from typing import List

def missingElement_TLE(nums: List[int], k: int) -> int:
    minimum = nums[0]
    maximum = nums[-1]

    missing_elements_arr = [0 for _ in range(k)]
    count = 0
    nums = set(nums)
    for i in range(minimum, maximum + 1):
        if i in nums:
            continue
        else:
            missing_elements_arr[count] = i
            count += 1
            if count == k:
                break

    if count < k:
        left_over = k - count
        for i in range(maximum + 1, maximum + left_over + 1):
            missing_elements_arr[count] = i
            count += 1

    return missing_elements_arr[-1]

def missingElement(nums: List[int], k: int) -> int:
    missing = lambda idx: nums[idx] - nums[0] - idx

    n = len(nums)

    if k > missing(n-1):
        return nums[-1] + k - missing(n-1) # this is for cases, where it goes beyond the range

    idx = 1 # idx = 0 would be 0, since no missing there
    while missing(idx) < k: # find a index such that missing[idx - 1] < k <= missing[idx]
        idx += 1

    # at the kth index, we can say there are missing[idx] - missing[idx-1] missing numbers
    # eg: missing[idx] = 3 and missing[idx-1] = 1 => there are total of 2 missing numbers between them
    # our k lies between these 2 missing numbers => to figure out => we can get it from nums[idx-1] + k - missing[idx-1]
    # eg: nums[idx-2] = 4, nums[idx-1] = 6, nums[idx] = 9, k = 2 => in between idx-1 and idx there are 3 missing number => k = 3
    # if we are asked 4th missing number => 2 would already b there b/w nums[idx-2] and nums[idx-1]
    # we come to a conclusion there are 2 more =>
    # so nums[idx-1] + k - missing[idx-1] => 6 + 3 - 2 (2 means previous missing values)
    return nums[idx-1] + k - missing(idx-1)


def missingElement_binaryApproach(nums: List[int], k: int) -> int:
    missing = lambda idx: nums[idx] - nums[0] - idx

    n = len(nums)

    if k > missing(n-1):
        return nums[-1] + k - missing(n-1) # this is for cases, where it goes beyond the range

    left = 0
    right = n - 1
    while left < right:
        pivot = (left + right) // 2

        if missing(pivot) < k:
            left = pivot + 1
        else:
            right = pivot

    return nums[left - 1] + k - missing(left - 1)

    
missingElement([4, 7, 9, 10], 7)
missingElement([1, 2, 4], 3)
