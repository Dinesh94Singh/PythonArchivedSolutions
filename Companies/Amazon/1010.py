"""
1010. Pair of songs with total durations divisible by 60

https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""

"""
n a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 
Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500

Hints: 

    - We can count the number of songs with (length % 60) equal to r, and store that in an array of size 60.
"""

from typing import List

def number_divisible_by_60(time: List) -> List:
    aux_dict = dict(enumerate([0] * 60))
    for duration in time:
        aux_dict[duration % 60] += 1
    n_pairs = 0
    if aux_dict[0] > 1:
        n_pairs += aux_dict[0] * (aux_dict[0] - 1) // 2
    if aux_dict[30] > 1:
        n_pairs += aux_dict[30] * (aux_dict[30] - 1) // 2
    for i in range(1, 30): # iterate the half and compare with the other half
        n_pairs += aux_dict[i] * aux_dict[60 - i]

    return n_pairs

number_divisible_by_60([30,20,150,100,40])