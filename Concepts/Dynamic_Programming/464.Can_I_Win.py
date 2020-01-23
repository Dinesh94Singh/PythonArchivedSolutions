"""
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.
"""

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def rec_helper(nums, remaining_total):
            nonlocal cache
            hash = str(nums)
            
            if hash in cache:
                return cache[hash]
            
            if nums[-1] > remaining_total:
                cache[hash] = True
                return True
            
            for i in range(len(nums)):
                if not rec_helper(nums[:i] + nums[i+1:], remaining_total - nums[i]):
                    cache[hash] = True
                    return True
            
            cache[hash] = False
            return False

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        cache = {}
        return rec_helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)
        