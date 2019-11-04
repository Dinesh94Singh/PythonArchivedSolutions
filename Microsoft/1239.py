"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""

def maxLength(arr):
    # subsets ?? and check length
    subsets = [""]
    for each in arr:
        n = len(subsets)
        for idx in range(n):
            subset = subsets[idx]
            subset += each
            subsets.append(subset)
    print(subsets)
    ans = (float('-inf'), "")
    for each in subsets:
        uniq_chars = set()
        valid = True
        for idx in range(len(each)):
            if each[idx] in uniq_chars:
                valid = False
                break
            else:
                uniq_chars.add(each[idx])
        print(uniq_chars)
        if valid:
            if ans[0] < len(uniq_chars):
                ans = (len(uniq_chars), each)
            else:
                # answer already has the better answer
                pass
    return len(ans[1])


def maxLength_optimized(arr):
    def hasDuplicates(s):
        return len(s) > len(set(s))
    def dfs(index, s):
        nonlocal maxLen
        maxLen = max(len(s), maxLen)

        if index == len(arr):
            return

        for i in range(index, len(arr)):
            if not hasDuplicates(s + arr[i]):
                dfs(i + 1, s + arr[i])
    if not arr:
        return 0
    maxLen = float('-inf')
    dfs(0, "")
    return maxLen

print(maxLength_optimized(["un","iq","ue"]))
