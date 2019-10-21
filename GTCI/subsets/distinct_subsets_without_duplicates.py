"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]

"""


def find_subsets(nums):
    nums.sort()
    subsets = [[]]
    start_idx, end_idx = 0, 0
    for idx, each_num in enumerate(nums):
        if idx > 0 and nums[idx] == nums[idx - 1]:
            start_idx = end_idx - 1
        end_idx = len(subsets)
        print('range is ', start_idx, end_idx)
        for i in range(start_idx, end_idx):
            each_set = subsets[i]
            subset = list(each_set)
            print('subset is ', subset, 'each set is', each_set)
            subset.append(each_num)
            subsets.append(subset)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
