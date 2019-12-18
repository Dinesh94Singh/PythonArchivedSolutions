import collections

class Solution():
    def findLadders(self, beginWord, endWord, wordList):
        possible_combinations = collections.defaultdict(list)
        for each_word in wordList:
            for i in range(len(each_word)):
                s = each_word[: i] + '#' + each_word[i+1:]
                possible_combinations[s].append(each_word)

        # print(possible_combinations)

        visited = set()
        self.ans = []
        self.min_length = float('inf')
        queue = collections.deque([(beginWord, 0, [beginWord])])

        while queue:
            for _ in range(len(queue)):
                word, level, words = queue.popleft()
                visited.add(word)
                if word == endWord:
                    if len(words) < self.min_length:
                        self.min_length = len(words)
                        self.ans.clear()
                        self.ans.append(words)
                    elif len(words) == self.min_length:
                        self.ans.append(words)

                for i in range(len(word)):
                    s = word[: i] + '#' + word[i + 1:]

                    for each_possibility in possible_combinations[s]:
                        if each_possibility not in visited:
                            queue.append((each_possibility, level + 1, words + [each_possibility]))
        return self.ans
        # return 0



s = Solution()
print(s.findLadders('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
