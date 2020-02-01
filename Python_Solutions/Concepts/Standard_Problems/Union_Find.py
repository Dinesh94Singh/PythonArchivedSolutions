"""
Union Find approach
"""

from typing import List


class DisjointSet(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, c1, c2):
        x, y = self.find(c1), self.find(c2)
        if x == y:
            pass
        else:
            if self.rank[x] > self.rank[y]:
                self.parents[y] = x
            else:
                self.parents[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
        return
