"""

238. Product of Array Except itself

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""


def productExceptSelf_BruteForce(nums):
    output = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i == j:
                continue
            prod = prod * nums[j]
        output.append(prod)
    print(output)


# O(n^2)


'''

Solution:

Instead of dividing the product of all the numbers in the array by the number at a given index to get the corresponding product, we can make use of the product of all the numbers to the left and all the numbers to the right of the index. Multiplying these two individual products would give us the desired result as well.

Input Array: 4, 5, 1, 8, 2
Left Prod: 1, 4, 20, 20, 160
Right Prod:  (starts from right end) 80, 16, 16, 2, 1
Left * Right = 80, 62, 320, 40, 160

'''


def productExceptSelf(nums):
    left_array = [1] * len(nums)
    right_array = [1] * len(nums)
    for i in range(1, len(nums)):
        left_array[i] = left_array[i - 1] * nums[i - 1]
    for j in range(len(nums) - 2, -1, -1):
        right_array[j] = right_array[j + 1] * nums[j + 1]
    print(left_array)
    print(right_array)
    return [left_array[i] * right_array[i] for i in range(len(nums))]


def product_except_self_constant_space(nums):
    length = len(nums)
    ans = [0] * length
    ans[0] = 1
    for i in range(1, length):
        ans[i] = ans[i-1] * nums[i-1]
    print(ans)
    temp = 1
    for i in reversed(range(length)):
        ans[i] = ans[i] * temp
        temp *= nums[i]
    print(ans)
    return ans


product_except_self_constant_space([4, 5, 1, 8, 2])


def productExceptSelf_retry(nums):
    left = [1 for _ in range(len(nums))]
    right = [1 for _ in range(len(nums))]

    for idx in range(1, len(nums)):
        left[idx] = left[idx - 1] * nums[idx - 1]

    print(left)

    temp = 1
    for i in reversed(range(len(nums))):
        right[i] = right[i] * temp
        temp *= nums[i]

    print(right)

    return [left[i] * right[i] for i in range(len(nums))]

productExceptSelf_retry([1, 2, 3, 4])

