"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longest_common_prefix_divide_conquer(strs) -> str:
    left, right = 0, len(strs) - 1

    def get_prefix(a, b):
        a_chars = list(a)
        b_chars = list(b)
        min_len = min(len(a_chars), len(b_chars))
        common_prefix = ''
        for i in range(min_len):
            if a_chars[i] == b_chars[i]:
                common_prefix += a_chars[i]
            else:
                return common_prefix
        return common_prefix

    def divide_conquer(left, right):
        if left == right:
            return strs[left]
        mid = (left + right) // 2
        left_str = divide_conquer(left, mid)
        right_str = divide_conquer(mid + 1, right)
        return get_prefix(left_str, right_str)

    return divide_conquer(left, right)


longest_common_prefix_divide_conquer(["flower", "flow", "flight"])
longest_common_prefix_divide_conquer(["dog", "racecar", "car"])


def longest_common_prefix_binary_search(strs):
    def is_common_prefix(end):
        base_str = strs[0][: end]
        for every_str in strs:
            if not every_str[:end] == base_str:
                return False
        return True

    min_len = float('inf')
    for each_str in strs:
        min_len = min(min_len, len(each_str))
    low, high = 0, min_len
    while low <= high:
        middle = (low + high) // 2
        if is_common_prefix(middle):
            low = middle + 1
        else:
            high = middle - 1
    return strs[0][: (low + high) // 2]


longest_common_prefix_binary_search(["flower", "flow", "flight"])
longest_common_prefix_binary_search(["dog", "racecar", "car"])


class Trie:
    def __init__(self, x):
        self.val = x
        self.next = None


def longest_common_prefix_trie(strs):
    base_str = list(strs[0])
    head = p1 = Trie(base_str[0])
    for idx in range(1, len(base_str)):
        p1.next = Trie(base_str[idx])
        p1 = p1.next
    for each_str in strs[1:]:
        p1 = head
        for each_char in list(each_str):
            if each_char == p1.val:
                p1 = p1.next
            else:
                break
        p1.val = None
        p1.next = None
    prefix = ''
    p1 = head
    while p1 and p1.val:
        prefix += p1.val
        p1 = p1.next
    return prefix


longest_common_prefix_trie(["flower", "flow", "flight"])
longest_common_prefix_trie(["dog", "racecar", "car"])
