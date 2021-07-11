import heapq
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def view_graph():
            nonlocal graph

            for each in graph:
                print(each, graph[each])

            print('\n\n')

        graph = collections.defaultdict(list)

        for each_ticket in tickets:
            dept, dest = each_ticket[0], each_ticket[1]
            heapq.heappush(graph[dept], dest)

        res = []
        dq = collections.deque(['JFK'])

        while dq:
            dept = dq[0]
            res.append(dept)
            destination = None
            if len(graph[dept]) > 0:
                destination = heapq.heappop(graph[dept])

            view_graph()

            if len(graph[dept]) == 0:
                dq.popleft()  # remove from the dq

            if destination:
                dq.appendleft(destination)

        return res


s = Solution()
print(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
