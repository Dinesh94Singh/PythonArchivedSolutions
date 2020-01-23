"""There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be
completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to
print all possible ordering of tasks meeting all prerequisites.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.
Example 2:

Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output:
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output:
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]
"""

from collections import deque
import copy


class Solution:
    def __init__(self):
        self.res = []

    def print_orders(self, tasks, prerequisites):
        in_degree = {each: 0 for each in range(tasks)}
        graph = {each: [] for each in range(tasks)}

        for each in prerequisites:
            in_degree[each[1]] += 1
            graph[each[0]].append(each[1])

        sources = []
        for each in in_degree.keys():
            if in_degree[each] == 0:
                sources.append(each)

        if len(sources) == 0:
            return 0

        self.retrieve_all_topological_sorts(graph, in_degree, sources, [])
        return self.res

    def retrieve_all_topological_sorts(self, graph, in_degree, sources, sorted_order):
        if sources:
            for vertex in sources:
                sorted_order.append(vertex)
                sources_for_next_call = deque(sources)
                sources_for_next_call.remove(vertex)
                for child in graph[vertex]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        sources_for_next_call.append(child)
                self.retrieve_all_topological_sorts(graph, in_degree, sources_for_next_call, sorted_order)

                # revert back
                sorted_order.remove(vertex)
                for child in graph[vertex]:
                    in_degree[child] += 1

        if len(sorted_order) == len(in_degree):
            print(sorted_order)


s = Solution()
print(s.print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))
