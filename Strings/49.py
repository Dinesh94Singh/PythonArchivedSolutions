"""

49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""

import collections


def group_anagrams(strs):
    dic = collections.defaultdict(list)
    ans = []
    for each_word in strs:
        dic[tuple(sorted(each_word))].append(each_word)
    for key, values in dic.items():
        ans.append(values)
    return ans


group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
