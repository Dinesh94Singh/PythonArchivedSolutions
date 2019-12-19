def canCompleteCircuit(gas, cost) -> int:
    tank = gap = start = 0
    for i in range(len(gas)):
        tank += gas[i]
        if tank >= cost[i]:
            tank -= cost[i]
        else:
            gap += cost[i] - tank
            print(gap)
            start = i + 1
            tank = 0
    if start == len(gas) or tank < gap: return -1
    return start


canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
