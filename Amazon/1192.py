"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

"""
import collections

class Solution:
    def critical_connections(self, n, connections):
        dic = collections.defaultdict(list)
        for c in connections:
            u, v = c
            dic[u].append(v)
            dic[v].append(u)

        timer = 0

        depth, lowest, parent, visited = [float("inf")] * n, [float("inf")] * n, [float("inf")] * n, [False] * n
        res = []

        def find(u):
            nonlocal timer

            visited[u] = True
            depth[u], lowest[u] = timer, timer
            timer += 1

            for v in dic[u]:
                if not visited[v]:
                    parent[v] = u
                    find(v)
                    if lowest[v] > depth[u]:
                        res.append([u, v])

                if parent[u] != v:
                    lowest[u] = min(lowest[u], lowest[v])

        find(0)
        return res

s = Solution()
print(s.critical_connections(4, [[0,1],[1,2],[2,0],[1,3]]))