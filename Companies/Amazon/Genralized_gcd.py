def generalizedGCD(num, arr):
    def gcd(x, y):
        if x > y:
            return gcd(y, x)
        elif x == 0:
            return y
        elif not x & 1 and not y & 1:  # x and y are even.
            return gcd(x >> 1, y >> 1) << 1
        elif not x & 1 and y & 1:  # x is even, y is odd.
            return gcd(x >> 1, y)
        elif x & 1 and not y & 1:  # x is odd, y is even.
            return gcd(x, y >> 1)
        return gcd(x, y - x)  # Both x and y are odd.
    if len(arr) == 0:
        return 0
    num1 = arr[0]
    num2 = arr[1]
    res = gcd(num1, num2)
    for idx in range(2, num - 1):
        res = gcd(res, arr[idx + 1])
    return res

print(generalizedGCD(5, [2, 3, 4, 5, 6]))
print(generalizedGCD(5, [2, 4, 6, 8, 10]))
