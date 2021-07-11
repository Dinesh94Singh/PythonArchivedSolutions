"""
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have
n
!
n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
"""


def find_permutations(nums):
    permutations = []
    state = [[]]
    for each_num in nums:
        n = len(state)
        for i in range(n):
            subset = state[i]
            for idx in range(len(subset) + 1):
                new_set = list(subset)
                new_set.insert(idx, each_num)
                if len(new_set) == len(nums):
                    permutations.append(new_set)
                else:
                    state.append(new_set)
    return permutations


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
