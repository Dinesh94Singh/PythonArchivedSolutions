'''
448. Find all numbers disappeared in an array.

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

Solution Idea: leet code

for each number i in nums, we mark the number that i points as negative.
Then we filter the list, get all the indexes who points to a positive number.
Since those indexes are not visited.
'''

def findDisappearedNumbers(nums):
  for i in range(len(nums)):
    idx = abs(nums[i]) - 1
    nums[idx] = -abs(nums[idx])
  print(nums)
  
  return [i+1 for i in range(len(nums)) if nums[i] > 0]

findDisappearedNumbers([4,3,2,7,8,2,3,1])