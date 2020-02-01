'''
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

'''

# def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

def maxSlidingWindow(nums, k):
    if len(nums) == 0 or len(nums) == 1 or len(nums) < k:
        return nums
    window_start = 0
    window_end = k - 1
    res = []
    while window_end < len(nums):
        print(window_end, window_start)
        res.append(max(nums[window_start: window_end+1]))
        window_start += 1
        window_end += 1
    return res

maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
maxSlidingWindow([], 2)
maxSlidingWindow([1], 2)
maxSlidingWindow([1, 2], 4)
