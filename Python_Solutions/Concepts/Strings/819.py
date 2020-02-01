"""

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.



Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.


Note:

1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.

"""
import collections


def most_common_word(paragraph, banned):
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
    print(paragraph)
    count = collections.Counter(word for word in paragraph.lower().split())

    for each in banned:
        del count[each]

    return count.most_common(1)[0][0]

def most_common_word_retry(paragraph, banned):
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
    print(paragraph)
    freq = collections.Counter(word for word in paragraph.lower().split())
    print(freq.most_common())
    for each_word, count in freq.most_common():
        if each_word in banned:
            continue
        else:
            return each_word

print(most_common_word_retry("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
