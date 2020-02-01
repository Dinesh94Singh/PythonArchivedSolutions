from collections import deque


def alienOrder(words):
    # using graph

    dependencies = []

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                dependencies.append([word1[j], word2[j]])  # since word1 comes before word2
                break

    print(dependencies)

    # form a graph and in_degree
    in_degree = {}
    graph = {}
    for each_word in words:
        for each_char in each_word:
            in_degree[each_char] = 0
            graph[each_char] = []

    # populate the graph
    for each_dependency in dependencies:
        in_degree[each_dependency[1]] += 1
        graph[each_dependency[0]].append(each_dependency[1])

    # get the sources and add it to queue - O(n)
    sources = []
    for each_key in in_degree:
        if in_degree[each_key] == 0:
            sources.append(each_key)
    print(sources)
    queue = deque(sources)

    # now we have list of sources, as we move ahead, figure out, if any of the dependency gets cleared off
    res = []
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            res.append(node)  # if its coming from queue, then it means, it is not dependent on anything else.

            for children in graph[node]:
                in_degree[children] -= 1
                if in_degree[children] == 0:
                    queue.append(children)  # we can further process this, since the dependency is removed

    return ''.join(res)


print(alienOrder(["za", "zb", "ca", "cb"]))
print(alienOrder(["ri", "xz", "qxf", "jhsguaw", "dztqrbwbm", "dhdqfb", "jdv", "fcgfsilnb", "ooby"]))
