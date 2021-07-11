"""
127. Word Ladder
"""
import collections


class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = collections.defaultdict(list)

    def visit_word_node(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladder_length(self, begin_word, end_word, word_list):
        if end_word not in word_list or not end_word or not begin_word or not word_list:
            return 0

        self.length = len(begin_word)

        for word in word_list:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        queue_begin = collections.deque([(begin_word, 1)])  # BFS starting from beginWord
        queue_end = collections.deque([(end_word, 1)])  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {begin_word: 1}
        visited_end = {end_word: 1}
        ans = None

        # We do a bi-directional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visit_word_node(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visit_word_node(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0


def ladderLength_my_sol(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    possible_combinations = collections.defaultdict(list)
    for each_word in wordList:
        for i in range(len(each_word)):
            s = each_word[: i] + '#' + each_word[i + 1:]
            possible_combinations[s].append(each_word)

    # print(possible_combinations)

    visited = set()
    queue = collections.deque([(beginWord, 0)])

    while queue:
        for _ in range(len(queue)):
            word, level = queue.popleft()
            visited.add(word)
            if word == endWord:
                return level + 1

            for i in range(len(word)):
                s = word[: i] + '#' + word[i + 1:]

                for each_possibility in possible_combinations[s]:
                    if each_possibility not in visited:
                        queue.append((each_possibility, level + 1))
    return 0
