class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check_palindrome(s_arr):
            length = len(s_arr)

            if length == 1 or length == 0:
                return True
            if length == 2:
                return s_arr[0] == s_arr[1]

            if length % 2 == 0:
                l, r = (length // 2) - 1, length // 2
            else:
                l, r = (length // 2) - 1, (length // 2) + 1

            while 0 <= l <= r < length and s_arr[l] == s_arr[r]:
                l -= 1
                r += 1
            return False if l != -1 or r != length else True

        s_arr = []
        for each in s:
            if each.isdigit() or each.isalpha():
                s_arr.append(each.lower())

        return check_palindrome(s_arr)