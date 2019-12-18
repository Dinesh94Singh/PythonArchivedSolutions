"""
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.
(The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring,
the answer is "".)



Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""
"""


def longest_duplicate_sub_string(s):
    def suffix_array(s):
        suf_array_map = {i: s[i:] for i in range(len(s))}
        return [element for element in
                sorted(suf_array_map.items(), key=lambda x: x[1])]

    def longest_common_prefix_array(s):
        def get_common_prefix(s1, s2):
            for i in range(min(len(s1), len(s2))):
                if s1[i] != s2[i]:
                    return i
            return i + 1

        suffix_array_matrix = suffix_array(s)

        res = [0]
        for i in range(1, len(suffix_array_matrix)):
            c = get_common_prefix(suffix_array_matrix[i - 1][1], suffix_array_matrix[i][1])
            res.append(c)

        return res

    def get_max_value_and_index(lcp_array):
        maximum, max_index = float('-inf'), float('-inf')

        for idx in range(len(lcp_array)):
            if maximum < lcp_array[idx]:
                maximum = lcp_array[idx]
                max_index = idx
        return maximum, max_index

    lcp_array = longest_common_prefix_array(s)
    # print(lcp_array)
    suf_arr = suffix_array(s)
    # print(suf_arr)

    max_value, index = get_max_value_and_index(lcp_array)
    for idx in range(len(suf_arr)):
        if idx == index:
            return suf_arr[idx][1][: max_value]
    return ""


# Solution using Rabin-Karp with Polynomial rolling hash.
class Solution:
    def search(self, L: int, a: int, modulus: int, n: int, nums) -> str:
        # Rabin-Karp => For first hash => prime ^ substring_index-0 * new_substring[0] + prime ^ substring_index-2 *
        # new_substring[1] + ..... n
        #
        # Rabin-Karp => ((prev_hash - prev_substring[0]) / prime) + prime ^ substring_index * new_substring[-1]

        # Calculate the hash of the substring [: L]
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus

        # already seen hashes of strings of length L
        seen = {h}
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

        pass

    def longest_duplicate_sub_string(self, s):
        # check if there is a duplicate substring for each substring possible =>
        left = 0
        right = len(s)

        # rolling hash
        a = 26
        modulus = 2 ** 32  # to avoid rolling hash

        nums = [ord(i) - ord('a') for i in s]

        while left <= right:
            mid = (left + (right - left)) // 2

            if self.search(mid, a, modulus, len(s), nums) != -1:
                left = mid + 1
            else:
                right = mid - 1

        start = self.search(left - 1, a, modulus, n, nums)
        return S[start: start + left - 1]


print(longest_duplicate_sub_string("ABRACADABRA"))
print(longest_duplicate_sub_string("banana"))
print(longest_duplicate_sub_string("abcd"))
