'''
442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]


Notes:

Similar to 448.

'''

# def findDuplicates(self, nums: List[int]) -> List

'''
This apporach only works because, of the input criteria that 1 <= a[i] <= n
'''

def findDuplicates(nums):
  res = []
  for x in nums:
    print(abs(x) - 1)
    if nums[abs(x) - 1] < 0:
      res.append(abs(x))
    else:
      nums[abs(x) - 1] *= -1
  return res
    
findDuplicates([4,3,2,7,8,2,3,1])