"""

557. Reverse words in string 3

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

"""


def reverse_words(s):
    words = s.split(" ")
    ans = ''
    for each_word in words:
        ans += each_word[::-1] + ' '

    return ans.strip()


reverse_words("Let's take LeetCode contest")
