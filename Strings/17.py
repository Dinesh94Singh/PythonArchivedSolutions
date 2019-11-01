"""

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""


def letter_combinations(digits):
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def back_track(combination, digits):
        if len(digits) == 0:
            output.append(combination)
        else:
            for each_letter in phone[digits[0]]:
                back_track(combination + each_letter, digits[1:])

    output = []
    back_track("", digits)
    return output

def letter_combinations_retry(digits):
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    subsets = [[]]
    res = []

    for each_digit in digits:
        n = len(subsets)
        for idx in range(n):
            for each_char in phone[each_digit]:
                sub_set = list(subsets[idx])
                sub_set.append(each_char)
                subsets.append(sub_set)
    for each_subset in subsets:
        if len(each_subset) == len(digits):
            res.append(''.join(each_subset))
    return res

letter_combinations_retry("234")
# letter_combinations("23456")
