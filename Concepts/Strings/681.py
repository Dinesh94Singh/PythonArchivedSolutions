"""

681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34",
"12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.


"""
import itertools


def next_closest_time(time):
    accepted_digits = {int(x) for x in time if x != ':'}
    hours, minutes = int(time[:2]), int(time[3:])
    ans = start = hours * 60 + minutes
    elapsed = 24 * 60
    for h1, h2, m1, m2 in itertools.product(accepted_digits, repeat = 4):
        hour = 10*h1 + h2
        min = 10*m1 + m2
        if hour < 24 and min < 60:
            current = hour * 60 + min
            candidate = (current - start) % (24 * 60)
            if 0 < candidate < elapsed:
                ans = current
                elapsed = candidate
    # ans is in min format - convert to hours and minutes
    # cur/60 & cur % 60

    output = '{:02d}:{:2d}'.format(ans // 60, ans % 60)
    return output


next_closest_time("01:34")
next_closest_time("19:34")
