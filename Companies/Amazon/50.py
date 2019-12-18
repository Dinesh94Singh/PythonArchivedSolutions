"""
50. My Pow
"""

"""
- n could be negative as well
- find the x power n


            2^5
        2^2     2^3
    2^1  2^1   2^2  2^1
2^0   

"""


class Solution_Recursive:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n//2)

class Solution_Iterative:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow