"""
https://leetcode.com/discuss/interview-question/365872/
"""


def equal_digit_sum(nums):
    def sum_of_digits(digit):
        total = 0
        while digit > 0:
            total += digit % 10
            digit //= 10
        return total

    res = float('-inf')
    cache = {}
    for each in nums:
        digit_sum = sum_of_digits(each)
        if digit_sum in cache:
            other_sum = cache[digit_sum]
            res = max(res, other_sum + each)
            cache[digit_sum] = max(cache[digit_sum], each)
        else:
            cache[digit_sum] = each
    return res if res != float('-inf') else -1


print(equal_digit_sum([51, 71, 17, 42]))
print(equal_digit_sum([42, 33, 60]))
print(equal_digit_sum([51, 32, 43]))
