import collections
class WordDistance:

    def __init__(self, words: List[str]):

        self.locations = collections.defaultDict(list)
        
        for index, value in enumerate(words):
            self.locations[value].append(index)
        

    def shortest(self, word1: str, word2: str) -> int:
        word1_indices = self.locations[word1]