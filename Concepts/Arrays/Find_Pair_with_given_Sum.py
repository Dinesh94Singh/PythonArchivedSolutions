"""
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.
Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.
"""
def two_sum(nums, target):
    target -= 30
    cache = {}
    res = []
    for idx, value in enumerate(nums):
        if value in cache:
            res.append([cache.get(value), idx])
        cache[target - value] = idx
    print(res)
    result = res[0]
    for each in res:
        if each[0] > result[0] or each[1] > result[1] or nums[each[0]] + nums[each[1]] > nums[result[0]] + nums[result[1]]:
            result = each
    return result

print(two_sum([1, 10, 25, 35, 60], 90))
print(two_sum([20, 50, 40, 25, 30, 10], 90))
