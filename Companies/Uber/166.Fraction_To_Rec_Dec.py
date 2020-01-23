"""
166. Fraction to recurring Decimal
"""


def fractionToDecimal(numerator: int, denominator: int) -> str:
    res = ''

    if numerator * denominator < 0:
        res += '-'

    numerator = abs(numerator)
    denominator = abs(denominator)

    # before point
    res += str(numerator // denominator)
    carrier = numerator % denominator

    # after point
    if carrier > 0:
        res += '.'
    memo = {}
    while carrier > 0:
        if carrier in memo:
            index = memo[carrier]
            res = res[:index] + '(' + res[index:] + ')'
            return res
        else:
            memo[carrier] = len(res)
            res += str((carrier * 10) // denominator)
            carrier = ((carrier * 10) % denominator)

    return res


# print(fractionToDecimal(2, 3))
# print(fractionToDecimal(1, 2))
print(fractionToDecimal(4, 333))
