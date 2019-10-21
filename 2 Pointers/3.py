"""

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }
}
"""


def lengthOfLongestSubstring(s):
    window_start = 0
    window_end = 0
    unique_chars = set()
    max_length = float("-inf")
    while window_end < len(s) and window_start <= window_end:
        if s[window_end] not in unique_chars:
            unique_chars.add(s[window_end])
            max_length = max(max_length, window_end - window_start + 1)
            window_end += 1
        else:
            unique_chars.remove(s[window_start])
            window_start += 1
    return max_length


lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("aabaab!bb")
lengthOfLongestSubstring("pwwkew")

# a a b a a b ! b b
# 0 1 2 3 4 5 6 7 8

# p w w k e w
# 0 1 2 3 4 5
