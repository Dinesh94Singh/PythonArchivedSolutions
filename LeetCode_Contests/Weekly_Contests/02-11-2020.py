from typing import List


def getNoZeroIntegers(n: int) -> List[int]:
    def check_for_non_zero(n):
        while n:
            quot, rem = divmod(n, 10)
            if rem == 0:
                return False
            n = quot
        return True

    if n < 2:
        return []  # guarenteed that there is going to be a solution, so this should not happen
    for i in range(n):
        a = i
        b = n - i

        if check_for_non_zero(a) and check_for_non_zero(b):
            return [a, b]
        else:
            continue


print(getNoZeroIntegers(1010))

"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ).
(bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

Example 1:
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:
Input: a = 4, b = 2, c = 7
Output: 1

Example 3:
Input: a = 1, b = 2, c = 3
Output: 0
 

Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
"""

"""
The idea is do column by column starting from right to left
- To move left you do x >> = 1
- To get the bit value x & 1 (gives the last bit)
"""


def minFlips(a: int, b: int, c: int) -> int:
    number_of_flips = 0
    while a != 0 and b != 0 and c != 0:
        x = a & 1
        y = b & 1
        z = c & 1

        if (x | y) != z:
            if x == 1 and y == 1:  # it means z is
                number_of_flips += 2
            else:
                number_of_flips += 1

        a >>= 1
        b >>= 1
        c >>= 1

    return number_of_flips


print(minFlips(4, 5, 6))
print(minFlips(4, 5, 11))
print("minFlips(2, 6, 5)", minFlips(2, 6, 5))
print("minFlips(8, 3, 5)", minFlips(8, 3, 5))

###################################################
import collections


def makeConnected(n: int, connections: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    inorder = collections.defaultdict(int)

    for each_conn in connections:
        a, b = each_conn
        graph[a].append(b)
        graph[b].append(a)
        inorder[b] += 1
        inorder[a] += 1

    remaining = 0
    for i in range(n):
        if inorder[i] == 0:
            remaining += 1

    duplicate_connections = 0
    for i in range(n):
        duplicate_connections += len(graph[i]) - 1 if len(graph[i]) > 1 else 1

    print(duplicate_connections // 2, remaining)

    if remaining > (duplicate_connections // 2):
        return -1
    else:
        return remaining


print(makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
