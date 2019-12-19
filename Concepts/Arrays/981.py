"""
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],
["foo","bar2",4],["foo",4],["foo",5]] Output: [null,null,"bar","bar",null,"bar2","bar2"] Explanation: TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1 kv.get("foo", 1);  // output
"bar" kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2,
then the only value is at timestamp 1 ie "bar" kv.set("foo", "bar2", 4); kv.get("foo", 4); // output "bar2" kv.get(
"foo", 5); //output "bar2"

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",
20],["love",5],["love",10],["love",15],["love",20],["love",25]] Output: [null,null,null,"","high","high","low","low"]


Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""

import collections


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((timestamp, value))
        self._map[key].sort(key=lambda x: x[0])  # sort based on timestamp

    def get(self, key: str, timestamp: int) -> str:
        values = self._map[key]
        left = 0
        right = len(values)
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
            elif values[mid][0] > timestamp:
                right = mid

        return "None" if right == 0 else values[right - 1][1]


class TimeMap2(object):
    def __init__(self):
        self.M = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.M[key].append((timestamp, value))

    def get(self, key, timestamp):
        A = self.M.get(key, None)
        if A is None: return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i - 1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# ["TimeMap","set","get","get","set","get","get"]
# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]

obj = TimeMap()
obj.set("foo", "bar", 10)
param_1 = obj.get("foo", 10)
print(param_1)
param_2 = obj.get("foo", 30)
print(param_2)
obj.set("foo", "bar2", 30)
param_3 = obj.get("foo", 10)
print(param_3)
param_4 = obj.get("foo", 5)
print(param_4)
param_5 = obj.get("foo", 15)
print(param_5)
