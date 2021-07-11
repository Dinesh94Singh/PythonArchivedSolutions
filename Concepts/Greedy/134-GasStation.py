# def canCompleteCircuit(gas, cost) -> int:
#     tank = gap = start = 0
#     for i in range(len(gas)):
#         tank += gas[i]
#         if tank >= cost[i]:
#             tank -= cost[i]
#         else:
#             gap += cost[i] - tank
#             print(gap)
#             start = i + 1
#             tank = 0
#     if start == len(gas) or tank < gap: return -1
#     return start
#
#
# canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])


#  EPI Solution
from typing import List

import collections

def canCompleteCircuit_epi(gas: List[int], cost: List[int]) -> int:
    # this solution guarentees to have a solution

    CostAndRemaining = collections.namedtuple('CostAndRemaining', ('city', 'rem_gas'))

    cost_rem_pair = CostAndRemaining(0, 0)

    total_no_of_stations = len(gas)
    total = 0
    for i in range(total_no_of_stations):
        total += gas[i] - cost[i]

    if total < 0:
        return -1

    remaining = 0

    for i in range(1, total_no_of_stations):
        remaining += gas[i - 1] - cost[i - 1]

        if remaining < cost_rem_pair.rem_gas:
            cost_rem_pair = CostAndRemaining(i, remaining)

    return cost_rem_pair


print(canCompleteCircuit_epi([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
