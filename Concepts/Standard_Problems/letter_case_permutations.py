"""
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""


def find_letter_case_string_permutations(word):
    permutations = [word]
    for idx, each_letter in enumerate(word):
        if not each_letter.isalpha():
            continue
        # can't directly loop in permutations because of mutual exclusion problem.
        n = len(permutations)
        for i in range(n):
            each_perm = permutations[i]
            letters = list(each_perm)
            letters[idx] = letters[idx].swapcase()
            print(letters)
            permutations.append(''.join(letters))

    return permutations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
