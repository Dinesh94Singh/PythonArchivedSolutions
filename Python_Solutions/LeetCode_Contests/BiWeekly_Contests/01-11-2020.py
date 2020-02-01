""" 01-11-2020 """

"""
5144. Matrix Block Sum
User Accepted:746
User Tried:871
Total Accepted:752
Total Submissions:1024
Difficulty:Medium
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements 
mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.


Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100

"""

from typing import List


def matrixBlockSum(mat: List[List[int]], K: int) -> List[List[int]]:
    m: int = len(mat)
    n: int = len(mat[0]) if m >= 0 else 0
    prefix_sum: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            prefix_sum[i+1][j+1] = mat[i][j] + prefix_sum[i + 1][j] + prefix_sum[i][j + 1]

    print(prefix_sum)


print(matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))

"""
5143. Decompress Run-Length Encoded List
User Accepted:1484
User Tried:1541
Total Accepted:1504
Total Submissions:1853
Difficulty:Easy
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, 
there are a elements with value b in the decompressed list. 

Return the decompressed list.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
 

Constraints:

2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
"""


def decompressRLElist(nums: List[int]) -> List[int]:
    res = []
    for i in range((len(nums) // 2)):
        print(i, 2 * i, 2 * i + 1)
        a = nums[2 * i]
        b = nums[2 * i + 1]

        for _ in range(a):
            res.append(b)

    return res


print(decompressRLElist([1, 2, 3, 4, 5]))

"""
5146. Distinct Echo Substrings
User Accepted:223
User Tried:402
Total Accepted:231
Total Submissions:721
Difficulty:Hard
Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself.

 

Example 1:

Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
Example 2:

Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
 

Constraints:

1 <= text.length <= 2000
text has only lowercase English letters.
"""


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        pass
