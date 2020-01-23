"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""

from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def is_prime(n):
            nonlocal factors
            for i in range(2, n):
                if n % i == 0:
                    factors.append(i)

        factors = []
        if n == 1 or is_prime(n):
            return factors

        res = []
        def backtracking_helper(factors, idx, prod_sub_arr, prod_val):
            if prod_val == n:
                res.append(prod_sub_arr)
            elif prod_val > n:
                return

            for i in range(idx, len(factors)):
                backtracking_helper(factors, i, prod_sub_arr + [factors[i]], prod_val * factors[i])

        backtracking_helper(factors, 0, [], 1)
        return res


s = Solution()
print(s.getFactors(12))
print(s.getFactors(32))
print(s.getFactors(1))
print(s.getFactors(7))