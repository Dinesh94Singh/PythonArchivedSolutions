"""
Given an
N
∗
N
N∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

Example 1:

Input:
Matrix=
[
  [2, 6, 8],
  [3, 7, 10],
  [5, 8, 11]
],
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
"""
from heapq import *


def find_Kth_smallest(k, matrix):
    minHeap = []

    # put the 1st element of each row in the min heap
    # we don't need to push more than 'k' elements in the heap
    for i in range(min(k, len(matrix))):
        heappush(minHeap, (matrix[i][0], i, 0))

    # take the smallest(top) element form the min heap, if the running count is equal to k' return the number
    # if the row of the top element has more elements, add the next element to the heap
    numberCount, number = 0, 0
    while minHeap:
        number, row, col = heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            break
        if len(row) > row+1:
            heappush(minHeap, (matrix[row+1][col], row+1, col))
        else:
            heappush(minHeap, (matrix[row][col+1], row, col+1))
    return number


find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)
