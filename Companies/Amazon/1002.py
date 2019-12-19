"""
1002. Find Common Characters
"""

"""

Given an array A of strings made only from lowercase letters,
return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three
times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter

"""

from typing import List
import string

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cnt = [float('inf')] * 26
        for s in A:
            cnt2 = [0] * 26
            for c in s:
                cnt2[ord(c) - ord('a')] += 1
            cnt = [min(cnt[i], cnt2[i]) for i in range(26)]
        return [c for k, c in zip(cnt, string.ascii_lowercase) for _ in range(k)]
        
s = Solution()
print(s.commonChars(["bella", "label", "roller"]))
