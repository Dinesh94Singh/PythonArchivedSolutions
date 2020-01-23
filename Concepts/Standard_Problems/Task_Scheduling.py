"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2]
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have cyclic dependency, therefore they cannot be sceduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible sceduling of tasks is: [0 1 4 3 2 5]
"""

def is_scheduling_possible(tasks, prerequisites):

    in_degree = { each: 0 for each in range(tasks) }
    graph = { each: [] for each in range(tasks) }

    for each in prerequisites:
        in_degree[each[1]] += 1
        graph[each[0]].append(each[1])

    sources = []
    for each in in_degree.keys():
        if in_degree[each] == 0:
            sources.append(each)
            
    return len(sources) != 0

is_scheduling_possible(3, [[0, 1], [1, 2]])
is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])
is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])
