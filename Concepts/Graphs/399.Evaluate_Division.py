from typing import List

import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def bfs(query):
            nonlocal graph

            if graph.get(query[0], float('inf')) == float('inf'):
                # no answer
                return -1

            if query[0] == query[1]:
                return 1

            dq = collections.deque(graph[query[0]])
            visited = set()

            while dq:
                node, val = dq.popleft()

                visited.add(node)

                if node == query[1]:
                    return val

                for nxt_node, v in graph[node]:
                    if nxt_node not in visited:
                        dq.append((nxt_node, val * v))

            return -1

        graph = collections.defaultdict(list)

        for equation, value in zip(equations, values):
            graph[equation[0]].append((equation[1], value))
            graph[equation[1]].append((equation[0], 1 / value))

        res = []
        for each in queries:
            res.append(bfs(each))

        return res

    def calcEquation_UnionFind(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        pass


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
s = Solution()
print(s.calcEquation(equations, values, queries))
