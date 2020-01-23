from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        anchor = -1
        i = 0
        while i < len(nums):
            if nums[i] == 0 and anchor == -1:
                anchor = i
            elif nums[i] == 0:
                pass
            elif anchor != -1:
                nums[i], nums[anchor] = nums[anchor], nums[i]
                anchor += 1

            i += 1

        return nums


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
