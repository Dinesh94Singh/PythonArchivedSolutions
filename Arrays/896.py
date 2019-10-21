"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if
for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
"""


def is_monotonic(arr):
    i = 0
    # increasing or decreasing ?
    direction = False
    while i < len(arr) - 1:
        if arr[i] != arr[i + 1]:
            direction = arr[i] < arr[i + 1]
            break
        i += 1
    if i == len(arr):
        return True
    if direction:
        while i < len(arr) - 1:
            if not arr[i] <= arr[i + 1]:
                return False
            i += 1
    else:
        while i < len(arr) - 1:
            if not arr[i] >= arr[i + 1]:
                return False
            i += 1
    return True


is_monotonic([1, 2, 2, 3])
is_monotonic([1, 3, 2])
is_monotonic([1, 2, 4, 5])
is_monotonic([1, 1, 1])
is_monotonic([1, 1, 0, 2])


def is_monotonic_lc(A):
    return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1))


is_monotonic_lc([1, 1, 1])
