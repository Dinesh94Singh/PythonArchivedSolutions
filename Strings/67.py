"""

67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""


def add_binary(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    if a[-1] == '1' and b[-1] == '1':
        # Add a zero at the end and compute add_binary for 1 and 1. Compute add_binary because, there could be carry
        return add_binary(add_binary(a[0: -1], b[0: -1]), '1') + '0'
    elif a[-1] == '0' and b[-1] == '0':
        # both are zero
        return add_binary(a[0: -1], b[0: -1]) + '0'
    else:
        # either of them is 1.
        return add_binary(a[0: -1], b[0: -1]) + '1'


add_binary("1010", "1011")
