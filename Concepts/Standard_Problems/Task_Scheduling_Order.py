"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5]
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
"""

from collections import deque

def task_scheduling_order(tasks, prerequisites):

    in_degree = { each: 0 for each in range(tasks) }
    graph = { each: [] for each in range(tasks) }

    for each in prerequisites:
        in_degree[each[1]] += 1
        graph[each[0]].append(each[1])

    sources = []
    for each in in_degree.keys():
        if in_degree[each] == 0:
            sources.append(each)

    if len(sources) == 0:
        return 0

    q = deque(sources)
    sorted_order = []
    while q:
        x = q.popleft()
        sorted_order.append(x)
        for each_child in graph[x]:
            in_degree[each_child] -= 1
            if in_degree[each_child] == 0:
                q.append(each_child)

    return sorted_order if len(sorted_order) == tasks else 0

print(task_scheduling_order(3, [[0, 1], [1, 2]]))
print(task_scheduling_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))
print(task_scheduling_order(3, [[0, 1], [1, 2], [2, 0]]))
