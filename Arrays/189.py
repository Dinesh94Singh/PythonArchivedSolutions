'''
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


'''

''' one solution is to store the last k and append those at the first '''
# Using Reverse
def rotate(nums, k):
    def numReverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    k, n = k % len(nums), len(nums)
    if k:
        numReverse(0, n - 1)
        numReverse(0, k - 1)
        numReverse(k, n - 1)

def rotate_cyclic(nums, k):
    k = k % len(nums) # if k >= len(nums) then algorithm does the same thing as k = k % len(nums)
    start = 0 # starting point of chain-replacement
    curr = start
    tmp = nums[curr] # holds prev value
    for _ in range(len(nums)):
        curr = (curr + k) % len(nums)
        nums[curr], tmp = tmp, nums[curr]
        if start == curr and start < len(nums) - 1:
            start += 1
            curr = start
            tmp = nums[curr]
rotate_cyclic([1, 2, 3, 4, 5, 6, 7], 3)