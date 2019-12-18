'''
78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

# def subsets(self, nums: List[int]) -> List[List[int]]:

def dfs(nums, index, path, res):
  res.append(path)
  for i in range(index, len(nums)):
    dfs(nums, i+1, path+[nums[i]], res)

def subsets_dfs(nums):
  res = []
  nums.sort()
  dfs(nums, 0, [], res)
  return res

def subsets_iterative(nums):
  res = []
  nums.sort()
  for num in nums:
    res += [item+[num] for item in res]
  return res

# Revist this while doing bit manipulation
def subsets_bitManipulation(nums):
  res = []
  nums.sort()
  for i in range(i<<len(nums)):
    tmp = []
    for j in range(len(nums)):
      if i & 1 << j:
        tmp.append(nums[j])
      res.append(tmp)
  return res