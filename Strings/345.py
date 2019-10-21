"""

345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

"""


def reverse_vowels(s):
    l, r = 0, len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    while l <= r:
        while l <= r and s[l] not in vowels: l += 1
        while l <= r and s[r] not in vowels: r -= 1
        if l > r:
            break
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return ''.join(s)


reverse_vowels("hello")
reverse_vowels("leetcode")
