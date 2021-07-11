from typing import List
import collections

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class DisjointSet(object):
            def __init__(self, n):
                self.parents = list(range(n))
                self.rank = [0] * n

            def find(self, i: int) -> int:
                if self.parents[i] != i:
                    self.parents[i] = self.find(self.parents[i])
                return self.parents[i]

            def union(self, c1, c2) -> bool:
                x, y = self.find(c1), self.find(c2)
                if x == y:
                    return False
                else:
                    if self.rank[x] > self.rank[y]:
                        self.parents[y] = x
                    else:
                        self.parents[x] = y
                        if self.rank[x] == self.rank[y]:
                            self.rank[y] += 1
                    return True

        
        djs = DisjointSet(n)
        for each_edge in edges:
            if not djs.union(each_edge[0], each_edge[1]):
                return False
        return len(edges) == n
        
        


s = Solution()
print(s.validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(s.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))