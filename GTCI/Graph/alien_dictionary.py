"""
There is a dictionary containing words from an alien language for which we don’t know the ordering of the characters. Write a method to find the correct order of characters in the alien language.

Example 1:

Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
from the given words we can conclude the following ordering among its characters:

1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

From the above two points we can conclude that the correct character order is: "bac"
Example 2:

Input: Words: ["cab", "aaa", "aab"]
Output: cab
Explanation: From the given words we can conclude the following ordering among its characters:

1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'

From the above two points, we can conclude that the correct character order is: "cab"
Example 3:

Input: Words: ["ywx", "xww", "xz", "zyy", "zwz"]
Output: yxwz
Explanation: From the given words we can conclude the following ordering among its characters:

1. From "ywx" and "xww", we can conclude that 'y' comes before 'x'.
2. From "xww" and "xz", we can conclude that 'w' comes before 'z'
3. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
2. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'

From the above two points we can conclude that the correct character order is: "yxwz"
"""

from collections import deque


def alien_dictionary(words):
    # INITIALIZE THE GRAPH
    in_degree = {}
    graph = {}
    for word in words:
        for char in word:
            in_degree[char] = 0
            graph[char] = []

    # POPULATE THE GRAPH
    for i in range(len(words) - 1):
        parent, child = words[i], words[i + 1]
        for j in range(min(len(parent), len(child))):
            if parent[j] != child[j]:
                in_degree[child[j]] += 1
                graph[parent[j]].append(child[j])
                break

    print(graph)
    print(in_degree)

    sources = []
    for each_vertex in graph:
        if in_degree[each_vertex] == 0:
            sources.append(each_vertex)

    # PERFORM TOPOLOGICAL SORT
    q = deque(sources)
    order = ''
    while q:
        x = q.popleft()
        order += x
        for child in graph[x]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                q.append(child)
    return order


alien_dictionary(["ba", "bc", "ac", "cab"])


class Solution:
    """
    [
      "wrt",
      "wrf",
      "er",
      "ett",
      "rftt"
    ]

    Output: "wertf"
    """
    
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        in_order = {}

        # at max we will have 26 chars

        for i in range(26):
            graph[i] = []
            in_order[i] = 0

        for i in range(len(words) - 1):
            curr_word, next_word = words[i], words[i+1]
            for j in range(min(len(curr_word), len(next_word))):
                if curr_word[j] < next_word[j]:
                    t1 = ord(next_word[j]) - 97
                    t2 = ord(curr_word[j]) - 97
                    
                    in_order[t1] += 1
                    graph[t2].append(t1)

        print(graph, in_order)

        sources = deque([])

        for i in range(26):
            if in_order[i] == 0:
                sources.append(i)

        print(sources)
        order = []

        while sources:
            node = sources.popleft()
            for each_child in graph[node]:
                in_order[each_child] -= 1
                if in_order[each_child] == 0:
                    sources.append(each_child)
        