"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def print_words(words):
            for each in words:
                print(each)

            print('\n\n\n')

        def check_word_squares(intermediate_words):
            # transpose of an matrix ??
            nonlocal res
            print_words(intermediate_words)
            for i in range(len(intermediate_words)):
                word = intermediate_words[i]
                another_word = ''.join([intermediate_words[k][i] for k in range(len(intermediate_words[0]))])
                print(word, another_word)
                if word != another_word:
                    return
            res.append(intermediate_words.copy())

        def rec_helper(intermediate_words: List, word_idx: int):
            if word_idx == len(words):
                check_word_squares(intermediate_words)
                return

            word = words[word_idx]
            for i in range(len(intermediate_words) + 1):
                intermediate_words.insert(i, word) # add
                rec_helper(intermediate_words, word_idx + 1)
                intermediate_words.pop(i) # remove

        res = []
        rec_helper([], 0)
        return res

s = Solution()
words = ["ball","area","lead","lady"]
print(s.wordSquares(words))