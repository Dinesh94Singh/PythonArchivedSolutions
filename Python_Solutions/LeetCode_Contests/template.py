from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for each in strs:
            print(each)
            s = sorted(each)
            print(s)
            if s not in hm:
                hm[s] = []
            hm[s].append(each)
            
        return hm.values()

s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])