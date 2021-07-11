"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def rec_helper(idx, remaining_target, path):
            if remaining_target == 0:
                res.append(path)
                return
            if idx == len(candidates):
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] <= remaining_target:
                    rec_helper(i + 1, remaining_target - candidates[i], path + [candidates[i]])
                else:
                    # since already its larger, you won't find anything after this
                    break
        rec_helper(0, target, [])
        return res

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))

