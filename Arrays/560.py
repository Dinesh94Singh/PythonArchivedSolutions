'''

560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''

# Using cumlative sum
def subarray_sum_cummulative_sum(nums, k):
    count = 0
    for start in range(len(nums)):
        total = 0
        for end in range(start, len(nums)):
            total += nums[end]
            if k == total:
                count += 1
    return count

subarray_sum_cummulative_sum([1, 1, 1], 2)

def subarray_sum_hashmap(nums, k):
    count = 0
    total = 0
    dic = { 0: 1}
    for i in range(len(nums)):
        total += nums[i]
        if total - k in dic:
            count += dic[total - k]
        dic[total] = dic.get(total, 0) + 1
        print('count is', count)
        print('dictionary is', dic)
        print('\n')
    return count

subarray_sum_hashmap([1, 1, 1], 2)
subarray_sum_hashmap([3, 4, 7, 2, -3, 1, 4, 2], 7)