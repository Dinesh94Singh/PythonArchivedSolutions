'''
561. Array Partition - 1

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

'''

def arrayPairSum(nums):
  nums.sort()
  print('nums are', nums)
  _sum = 0
  for i in range(0, len(nums), 2):
    _sum += nums[i]
  print(_sum)

arrayPairSum([7, 3, 1, 0, 0, 6])


# using hashmap
# https://leetcode.com/problems/array-partition-i/discuss/102201/Python-solution-with-detailed-explanation
def arrayPairSum_hashMap(nums):
    res = [0]*20001
    for x in nums:
        res[x+10000] += 1
    s_so_far, adjust = 0, False
    for idx, freq in enumerate(res):
        if freq:
            freq = freq-1 if adjust else freq
            if freq&1:
                s_so_far += ((freq//2) + 1)*(idx-10000)
                adjust = True
            else:
                s_so_far += ((freq//2))*(idx-10000)
                adjust = False
    return s_so_far

arrayPairSum_hashMap([7, 3, 1, 0, 0, 6])