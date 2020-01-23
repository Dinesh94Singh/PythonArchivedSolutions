import collections
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], seq: str) -> bool:
        order_idx_map = {i: ch for i, ch in enumerate(seq)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:

                    if order_idx_map[word1[j]] > order_idx_map[word2[j]]:
                        # specifies, word1 came before word2 (which is right)
                        return False
                    elif len(word1) > len(word2):
                        return False

        return True


s = Solution()
# print(s.isAlienSorted(['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz'))
print(s.isAlienSorted(["kuvp", "q"], 'ngxlkthsjuoqcpavbfdermiywz'))
