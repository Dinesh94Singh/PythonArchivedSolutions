"""

344. Reverse a string

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


"""


def reverse(s):
    l = len(s) - 1
    for i in range(l // 2):
        s[i], s[l - i] = s[l - i], s[i]
    print(s)


reverse(["h", "e", "l", "l", "0"])
