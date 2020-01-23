"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""
from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm = {}
        for ch1, ch2 in zip(s, t):
            if ch1 in hm:
                if hm[ch1] != ch2:
                    return False
            else:
                if ch2 in hm.values():
                    return False
                hm[ch1] = ch2

        return True

    def groupIsomorphic(self, s: str, t: str) -> List[List[str]]:
        pass


sol = Solution()

s = 'paper'
t = 'title'
print(sol.isIsomorphic(s, t))

s = 'foo'
t = 'bar'
print(sol.isIsomorphic(s, t))

s = 'ab'
t = 'aa'
print(sol.isIsomorphic(s, t))

def isIsomorphic1(self, s, t):
    """
    Time Complexity O(nlogn)
    Space Complexity O(2n)
    """
    d1, d2 = {}, {}
    for i, val in enumerate(s):
        d1[val] = d1.get(val, []) + [i]
    for i, val in enumerate(t):
        d2[val] = d2.get(val, []) + [i]
    return sorted(d1.values()) == sorted(d2.values())
        
def isIsomorphic2(self, s, t):
    """
    Time Complexity O(nlogn)
    Space Complexity O(2n)
    """
    d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
    for i, val in enumerate(s):
        d1[ord(val)].append(i)
    for i, val in enumerate(t):
        d2[ord(val)].append(i)
    return sorted(d1) == sorted(d2)
    
def isIsomorphic3(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
def isIsomorphic4(self, s, t): 
    return [s.find(i) for i in s] == [t.find(j) for j in t]
    
def isIsomorphic5(self, s, t):
    return map(s.find, s) == map(t.find, t)

def isIsomorphic(self, s, t):
    """
    This sol is close to what I have implemented, instead of linear search while doing hm.values(), we create a reverse HM
    
    Time Complexity - O(n)
    Space Complexity - O(n)
    """
    d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
    for i in range(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i+1
        d2[ord(t[i])] = i+1
    return True