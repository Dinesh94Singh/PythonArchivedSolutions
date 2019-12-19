"""
402. Remove K digits
"""

"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number
is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = list(num)
        if len(s) == k:
            print('0')
            return
        idx = 0
        while idx < len(s) - 1 and k > 0:
            if int(s[idx]) > int(s[idx+1]):
                s = s[:idx] + s[idx + 1: ]
                k -= 1
            else:
                idx += 1
        if k != 0:
            s = s[:len(s)-k]
        print(str(int(''.join(s))))

s = Solution()
s.removeKdigits("10200", 1)
s.removeKdigits("10", 2)
s.removeKdigits("1432219", 3)
s.removeKdigits("9", 1)
s.removeKdigits("19", 2)
s.removeKdigits('112', 1)