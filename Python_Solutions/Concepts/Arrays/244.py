from typing import List
import collections


class WordDistance:

    def __init__(self, words: List[str]):
        self.word_index_map = collections.defaultdict(list)

        for idx, each in enumerate(words):
            self.word_index_map[each].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        a = self.word_index_map[word1]
        b = self.word_index_map[word2]

        min_dist = float('inf')
        for i in a:
            for j in b:
                if min_dist > abs(i - j):
                    min_dist = abs(i - j)

        return min_dist


# Your WordDistance object will be instantiated and called as such:
words = ["practice", "makes", "perfect", "coding", "makes"]
obj = WordDistance(words)
word1 = "coding"
word2 = "practice"
param_1 = obj.shortest(word1, word2)
print(param_1)

word1 = "makes"
word2 = "coding"
param_1 = obj.shortest(word1, word2)
print(param_1)
