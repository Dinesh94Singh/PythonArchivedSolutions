"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
from typing import List

from collections import deque
class Solution:
    def iterative(self, nums):
        res = [[]]
        for n in nums:
            temp = []
            for item in res:
                for i in range(len(item) + 1):
                    temp += item[:i] + [n] + item[i:],
                    if i < len(item) and item[i] == n:
                        break
            res = temp
        return res if any(res) else []    


    def permuteUnique_backtracking(self, nums: List[int]) -> List[List[int]]:
        def rec_helper(temp, size):
            if len(temp) == size:
                res.append(temp[:])

            for i in range(size):
                if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]): 
                    continue

                visited[i] = True
                temp.append(nums[i])
                rec_helper(temp, size)
                temp.pop()
                visited[i] = False
            
        res = []
        visited = [False] * len(nums) # since its primitive type, it is immutable
        rec_helper([], len(nums))
        return res

s = Solution()
print(s.permuteUnique_backtracking([1, 1, 2]))
print(s.iterative([1, 1, 2]))