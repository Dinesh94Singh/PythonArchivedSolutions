from typing import List

"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            Time Complexity => O(n!)
        """
        temp = [[]]
        perms = []
        
        for each_num in nums:
            for s in range(len(temp)): # python with range is good, it creates a range object.
                each_sub_set = temp[s]
                for i in range(len(each_sub_set) + 1):
                    new_list = list(each_sub_set)
                    new_list.insert(i, each_num)

                    if len(new_list) == len(nums):
                        perms.append(new_list)
                    else:
                        temp.append(new_list)
        return perms[::-1]

    def permute_backtracking(self, nums: List[int]) -> List[List[int]]:
        """
            Time Complexity => O(n!)
        """
        def rec_helper(start_idx, end_idx):
            if start_idx == end_idx:
                res.append(nums[:])
            for i in range(start_idx, end_idx):
                nums[start_idx], nums[i] = nums[i], nums[start_idx]
                rec_helper(start_idx + 1, end_idx)
                nums[start_idx], nums[i] = nums[i], nums[start_idx] # backtrack
        res = []
        rec_helper(0, len(nums))
        return res


s = Solution()
# print(s.permute([1,2,3]))
# print(s.permute([5, 4, 6, 2]))
print(s.permute([1, 2, 3]))
print(s.permute_backtracking([1, 2, 3]))