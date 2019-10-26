"""
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation:
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
"wagl" is repeated twice, but is included in the output once.
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26
"""

def length_of_all_substrings_with_k_dist_chars(s, k):
    s = list(s)
    uniq_chars = set()
    start = 0
    end = 0
    res = set()
    while end < len(s):
        ch = s[end]
        if ch not in uniq_chars or len(uniq_chars) < k:
            uniq_chars.add(ch)
        else:
            if end - start >= k:
                i = start
                j = start + k
                while j <= end + 1:
                    if len(set(s[i: j])) == k:
                        res.add(''.join(s[i: j]))
                    i += 1
                    j += 1
            start += 1
        end += 1
    return len(res)

print(length_of_all_substrings_with_k_dist_chars("abcabc", 3))
print(length_of_all_substrings_with_k_dist_chars("abacab", 3))
print(length_of_all_substrings_with_k_dist_chars("awaglknagawunagwkwagl", 4))
