"""

43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


"""


def multiply_ordinal(num1, num2):
    n1, n2 = 0, 0
    for each_char in num1:
        n1 = n1 * 10 + ord(each_char) - ord('0')
    for each_char in num2:
        n2 = n2 * 10 + ord(each_char) - ord('0')
    prod = n1 * n2
    return ""+str(prod)


multiply_ordinal('10', '10')


def multiply(num1, num2):
    product = [0] * (len(num1) + len(num2))
    position = len(product) - 1
    for n1 in reversed(num1):
        temp_pos = position
        for n2 in reversed(num2):
            a, b = int(n1), int(n2)
            product[temp_pos] += a * b
            product[temp_pos - 1] += product[temp_pos] // 10
            product[temp_pos] %= 10
            temp_pos -= 1
        position -= 1
    pt = 0
    while pt < len(product) - 1 and product[pt] == 0:
        # remove leading zero's
        pt += 1
    return ''.join(map(str, product[pt:]))


multiply('10', '10')
