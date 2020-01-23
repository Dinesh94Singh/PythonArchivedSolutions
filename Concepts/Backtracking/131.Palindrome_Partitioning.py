def partition(s):
    res = []
    dfs(s, [], res)
    return res


def dfs(s, path, res):
    if not s:
        res.append(path[:])  # creates a new list if you do :
        return  # backtracking
    for i in range(1, len(s) + 1):
        # we are not expanding around center, rather a, aa, aab, aaba, aabaa.
        if isPalindrome(s[:i]):
            path.append(s[:i])
            dfs(s[i:], path, res)
            path.pop()


def isPalindrome(s):
    return s == s[::-1]


print(partition("aab"))
print(partition("aabaa"))


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def check_palindrome(s):
            return s == s[::-1]

        def rec_helper(s, sub_arr):
            if not s:
                res.append(list(sub_arr))
                return

            for i in range(1, len(s) + 1):
                print(s[:i])
                if check_palindrome(s[:i]):
                    sub_arr.append(s[:i])
                    rec_helper(s[i:], sub_arr)
                    sub_arr.pop()

        rec_helper(s, [])
        return res


s = Solution()
print(s.partition("aab"))
