"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


def isHappy(n):
    def sum_sq(n):
        total = 0
        while n != 0:
            total += ((n % 10) ** 2)
            n = n // 10
        return total

    cache = set()
    cache.add(n)
    while n != 1:
        n = sum_sq(n)
        print(n)
        if n in cache:
            return False
        cache.add(n)
    return True

print(isHappy(19))