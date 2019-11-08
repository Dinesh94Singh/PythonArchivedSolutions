"""
Given a string s containing only a and b, find longest substring of s such that s does not contain more than two contiguous occurrences of a and b.

Example 1:

Input: "aabbaaaaabb"
Output: "aabbaa"
Example 2:

Input: "aabbaabbaabbaa"
Output: "aabbaabbaabbaa"
"""

def longest_substring_with_2_consequite_occurences(s):
    # TODO: Solve it your self - sliding window ( start = end = end - 1) ~ Hint ~
    start = 0
    end = 0
    count = 1
    ch = s[end]
    ans = (float('-inf'), 0, 0, '')
    while end < len(s):
        if s[end] == ch:
            count += 1
            if count > 2:
                # update the ans
                if ans[0] > end - start:
                    pass
                else:
                    ans = (end-start, start, end, s[start: end]) # end is exlusive here for getting the substring
                start = end - 1
                end = end - 1
                count = 1
        else:
            ch = s[end]
            count = 1
        end += 1
    if ans[0] < (end - start + 1):
        ans = (end-start, start, end, s[start: end])
    return ans

print(longest_substring_with_2_consequite_occurences("aababaaaaaa"))
print(longest_substring_with_2_consequite_occurences("aababaaaaabab"))
print(longest_substring_with_2_consequite_occurences("aaaaaaa"))
print(longest_substring_with_2_consequite_occurences("aababaaabbabbababaababababababa"))

def longest_substring_with_2_occurences(s):
    start = 0
    ans = (float('-inf'), 0, 0)
    cache = {'a': 0, 'b': 0}
    end = 0
    while end < len(s):
        if cache[s[end]] <= 1:
            # there is still place to increase
            cache[s[end]] += 1
            end += 1
            if ans[0] == max(ans[0], end-start):
                # old ans is better. or if end-start == ans[0] # if asked for multiple answers, just append here.
                continue
            else:
                # this is much better
                ans = (end-start, start, end-1)
        else:
            # we already reached the limit of 2 cons
            cache[s[start]] -= 1
            start += 1
    return ans

# print(longest_substring_with_2_occurences("aabbaaaaabb"))
# print(longest_substring_with_2_occurences("aaaaa"))
