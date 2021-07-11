"""
91. Decode Ways
"""

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

"""
    int numDecodings(string s) {
        return s.empty() ? 0: numDecodings(0,s);    
    }
    int numDecodings(int p, string& s) {
        int n = s.size();
        if(p == n) return 1;
        if(s[p] == '0') return 0;
        int res = numDecodings(p+1,s);
        if( p < n-1 && (s[p]=='1'|| (s[p]=='2'&& s[p+1]<'7'))) res += numDecodings(p+2,s);
        return res;
    }
"""

class Solution:
    def num_decoding(self, s: str) -> int:
        # 1 digit or 2 digit max => s-1 or s-2 ways

        def dfs(idx, length = len(s) - 1):
            nonlocal res
            if idx == length:
                return 1

            if s[idx] == '0':
                return 0

            res += dfs(idx+1)
            if (s[idx] == '1' or s[idx] == '2') and (int(s[idx+1]) < 7):
                res += dfs(idx+2)

            return res

        res = 0
        total_number_of_ways = dfs(0)

        return total_number_of_ways

s = Solution()
# print(s.num_decoding("12")) #ab or L
# print(s.num_decoding("226")) #22, 26, 2, 6
# print(s.num_decoding("20")) #
print(s.num_decoding("226")) # BZ

