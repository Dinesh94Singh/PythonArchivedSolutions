"""

Dijkstras Algorithm: => dist(b) = min(dist_reach_nei + cost_from_nei_to_b, prev_dist_to_reach_b)
===================
- Given a graph and a source vertex in the graph, find shortest paths from source to all vertices in the given graph.
- Without knowing the shortest path to all the vertices, you cannot confirm that, a particular path is the shortest path

- Like Prim’s MST, we generate a SPT (shortest path tree / Minimum Spanning Tree) with given source as root.

We maintain two sets,
    - one set contains vertices included in shortest path tree,
    - other set includes vertices not yet included in shortest path tree.

At every step of the algorithm, we find a vertex which is in the other set (set of not yet included) and has a minimum
distance from the source.

LeetCode Problems with Dijkstras - Find the solutions in Graph's tab

- https://leetcode.com/problems/cheapest-flights-within-k-stops/


Notes:
======

So when to use DFS over A*, when to use Dijkstra over A* to find the shortest paths ?
We can summarise this as below-

1) One source and One Destination-
→ Use A* Search Algorithm (For Unweighted as well as Weighted Graphs)

2) One Source, All Destination –
→ Use BFS (For Unweighted Graphs)
→ Use Dijkstra (For Weighted Graphs without negative weights)
→ Use Bellman Ford (For Weighted Graphs with negative weights)

3) Between every pair of nodes-
→ Floyd-Warshall
→ Johnson’s Algorithm

"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")

        for node in range(self.V):
            print(node, "t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        minimum = float('inf')

        # Search not nearest vertex not in the
        # shortest path tree
        for each_vertex in range(self.V):
            if dist[each_vertex] < minimum and sptSet[each_vertex] == False:
                minimum = dist[each_vertex]
                min_index = each_vertex

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):

            # Pick the minimum distance vertex from the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the shortest path tree
            sptSet[u] = True  # mark visited

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

    # Driver program


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.dijkstra(0);