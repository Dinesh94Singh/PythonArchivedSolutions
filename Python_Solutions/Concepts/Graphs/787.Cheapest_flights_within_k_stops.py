"""

787. https://leetcode.com/problems/cheapest-flights-within-k-stops/


There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the
cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
=========
Input: n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
=========
Input: n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.



Note:
- The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
- The size of flights will be in range [0, n * (n - 1) / 2].
- The format of each flight will be (src, dst, price).
- The price of each flight will be in the range [1, 10000].
- k is in the range of [0, n - 1].
- There will not be any duplicated flights or self cycles.

Dijkstras algorithm

"""

from typing import List
from heapq import heappush, heappop
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, total_allowed_stops: int) -> int:
        graph = collections.defaultdict(dict)
        for _from, to, wt in flights:
            graph[_from][to] = wt

        best_path = {}

        pq = [(0, 0, src)]  # (cost, total_stops, src)

        while pq:
            cost, k, city = heappop(pq)

            if k > total_allowed_stops + 1 or cost > best_path.get((k, city), float('inf')):
                # do we really need to check cost > best_path again here? Aren't we checking and adding in below. - No
                # tests pass after removing the above cond
                continue

            if city == dst:
                # why are we returning as soon as we reach dst ? - You don't need to, the below code, checks and returns
                return cost

            for nei, wt in graph[city].items():
                new_cost = cost + graph[city][nei]

                if new_cost < best_path.get((k + 1, nei), float('inf')):
                    heappush(pq, (new_cost, k + 1, nei))
                    best_path[(k + 1, nei)] = new_cost

        min_cost = float('inf')
        print(best_path)
        for each in best_path:
            if each[1] == dst and each[0] <= total_allowed_stops + 1:
                min_cost = min(min_cost, best_path[each])
        return -1 if min_cost == float('inf') else min_cost


s = Solution()
print(s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
