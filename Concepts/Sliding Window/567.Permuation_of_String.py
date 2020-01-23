from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            s2, s1 = s1, s2

        char_freq_s1 = Counter(s1)

        start = 0
        end = len(s1)

        while end <= len(s2):
            char_freq_subwindow = Counter(s2[start: end])

            found = True

            for ch, freq in char_freq_s1.items():
                if char_freq_subwindow.get(ch, -1) != freq:
                    found = False
                    break

            if found:
                return True

            end += 1
            start += 1

        return False
    

s = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(s.checkInclusion(s1, s2))
s1 = "ab"
s2 = "eidboaoo"
print(s.checkInclusion(s1, s2))
s1 = "ab"
s2 = "eidboaab"
print(s.checkInclusion(s1, s2))
s1 = "ab"
s2 = "aebidaboa"
print(s.checkInclusion(s1, s2))
