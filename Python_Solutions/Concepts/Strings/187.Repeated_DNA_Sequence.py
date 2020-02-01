"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""
from typing import List


# O(n^2) with each window size of 10 chars => you try to find if that sequence occurence more than once.
# If it has occured, add it to the list
# If the given DNA is too huge, then you have to use KMP algorithm or Rabin Karp Algorithm
# KMP algorithm Applications in LC -> Repeating Substring, Duplicate Substring, Common Substring etcs

def find_repeated_dna_sequences_bf(s: str) -> List[str]:
    _set = set()
    for i in range(len(s) - 10 + 1):
        start_idx = i
        end_idx = i + 10
        string = s[start_idx: end_idx]
        for j in range(i + 1, len(s) - 10 + 1):
            if s[j: j+10] == string:
                _set.add(s[j: j+10])

    return list(_set)

def find_repeated_dna_sequences_with_extra_space(s: str) -> List[str]:
    hm = {}
    for i in range(len(s) - 10 + 1):
        if s[i: i + 10] in hm:
            hm[s[i: i + 10]] += 1
        else:
            hm[s[i: i + 10]] = 1

    res = []
    for key, val in hm.items():
        if val > 1:
            res.append(key)
    
    return res

print(find_repeated_dna_sequences_bf("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(find_repeated_dna_sequences_bf("AAAAAAAAAAA"))

print(find_repeated_dna_sequences_with_extra_space("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(find_repeated_dna_sequences_with_extra_space("AAAAAAAAAAA"))

def findRepeatedDnaSequences(self, n: str) -> List[str]:
    if len(n) < 10: return []
    l, k = len(n), 10
    a = 4
    mod = l * l * k # alternative to 2**31
    aL = pow(a, k, mod)
    
    seen, keep = {}, set()
    
    to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    _n = [to_int.get(s) for s in n]
    
    h = 0
    for i in range(k):
        h = (a * h + _n[i]) % mod
        
    seen[h] = n[:k]
    for i in range(1, l - k + 1):
        h = (h * a - _n[i - 1] * aL + _n[i + k - 1] % mod) % mod
        if h in seen:
            keep.add(seen[h])
        else:
            seen[h] = n[i:i + k]

    return list(keep)