def solution(num):
    if num < 0:
        return neg(num)
    else:
        return pos(num)


def pos(num):
    n = len(str(num))
    res = 0

    while num >= 0:
        val = num // 10 ** (n - 1)
        num %= 10 ** (n - 1)
        if val < 5:
            res += (5 * 10 ** n) + val * (10 ** (n - 1)) + num
            return res
        else:
            res += val * 10 ** n
            n -= 1


def neg(num):
    num = abs(num)
    n = len(str(num))
    res = 0

    while num >= 0:
        val = num // 10 ** (n - 1)
        num %= 10 ** (n - 1)
        if val > 5:
            res += (5 * 10 ** n) + val * (10 ** (n - 1)) + num
            return -res
        else:
            res += val * 10 ** n
            n -= 1


print(solution(-99))