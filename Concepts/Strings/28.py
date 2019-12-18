"""

28. implement strStr

"""


def str_str(haystack, needle):
    n = len(needle)

    for i in range(len(haystack) - n + 1):
        if haystack[i:i + n] == needle:
            return i

    return -1


str_str("ababa", "baba")


