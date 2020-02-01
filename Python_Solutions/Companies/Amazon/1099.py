"""
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.



Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation:
In this case it's not possible to get a pair sum less that 15.


Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""


class Solution:
    def twoSumLessThanK_brute_force(self, A, K):
        # O(n2)
        res = []
        maxi = float('-inf')
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j:
                    continue
                else:
                    total = A[i] + A[j]
                    if maxi < total < K:
                        maxi = total
        return maxi

    def twoSumLessThanK_sorted(self, A, K):
        # O(nlogn)
        A.sort()
        i = 0
        j = len(A) - 1
        max = float('-inf')
        while i < j:
            total = A[i] + A[j]
            if K > total:
                if total > max:
                    max = total
                i += 1
            else:
                j -= 1
        return max


s = Solution()
print(s.twoSumLessThanK_brute_force([34,23,1,24,75,33,54,8], 60))
print(s.twoSumLessThanK_sorted([34,23,1,24,75,33,54,8], 60))