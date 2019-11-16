"""
472. Concatenated Words
"""


def findAllConcatenatedWordsInADict(words):
    words_dict = set(words)

    def dfs(remaining):
        for i in range(len(remaining)):
            if remaining[: i + 1] in words_dict and remaining[i + 1:] in words_dict:
                return True
            if remaining[: i + 1] in words_dict and dfs(remaining[i + 1:]):  # can be a combination of 2 or more words
                return True
            # if remaining[i + 1:] in words_dict and dfs(remaining[: i + 1]):  # can be a combination of 2 or more words
            #     return True
        return False

    res = []
    for each in words:
        if dfs(each):
            res.append(each)
    return res


findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"])
