"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to
find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as
[1, 0] and thus will not appear together in edges.

"""
from typing import List

class Solution:
    def countComponents_dfs_solution(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []

        for each_edge in edges:
            graph[each_edge[0]].append(each_edge[1])
            graph[each_edge[1]].append(each_edge[0])

        visited = set()

        def dfs(vertex):
            visited.add(vertex)
            other_vertices = graph[vertex]

            for each in other_vertices:
                if each not in visited:
                    dfs(each)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res

    def countComponents_bfs_solution(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []

        for each_edge in edges:
            graph[each_edge[0]].append(each_edge[1])
            graph[each_edge[1]].append(each_edge[0])

        res = 0

        for i in range(n):
            queue = [i]
            res += 1 if i in g else 0
            for j in queue: # explore all paths from j => could use normal bfs as well.
                if j in graph:
                    queue += graph[j] # don't like the idea of modifying while looping, use normal bfs
                    del graph[j]
        return res