"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


def letter_combinations(digits):
    phone_dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    subsets = [[]]
    for each_digit in digits:
        alphabets = phone_dic.get(each_digit)
        length = len(subsets)
        for each_alpha in alphabets:
            for idx in range(length):
                subset = list(subsets[idx])
                subset.append(each_alpha)
                subsets.append(subset)
    print(subsets)
    filtered_results = filter(lambda x: len(x) == 2, subsets)
    results = []
    for each in filtered_results:
        results.append(''.join(each))
    return results


print(letter_combinations("23"))
