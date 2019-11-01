"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n, count):
            nonlocal cache
            if n == 0:
                count += 1
                return count
            elif n == 1:
                return helper(n-1, count)
            else:
                l, r = 0, 0
                if n - 2 not in cache:
                    l = helper(n-2, count)
                    cache[n-2] = l
                else:
                    l = cache[n-2]
                if n - 1 not in cache:
                    r = helper(n-1, count)
                    cache[n-1] = r
                else:
                    r = cache[n-1]
                return l + r
        count = 0
        cache = {}
        return helper(n, 0)

s = Solution()

print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(35))
print(s.climbStairs(10))
