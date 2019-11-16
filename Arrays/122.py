'''

122. Best time to buy and sell stocks - 2

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''


# Approach 1 - Brute Force

def cal(prices, s):
    if s >= len(prices):
        return 0
    max_val = 0
    for start in range(s, len(prices)):
        max_profit = 0
        for i in range(start + 1, len(prices)):
            if prices[start] < prices[i]:
                profit = cal(prices, i + 1) + prices[i] - prices[start]
                if profit > max_profit:
                    max_profit = profit
        if max_profit > max_val:
            max_val = max_profit
    return max_val


def maxProfit_bruteForce(prices):
    return cal(prices, 0)


# Approach 2 - find the max and min

def maxProfit_2(prices):
    max_profit = 0
    n = len(prices) - 1
    i = 0
    while i < n - 1:
        # find valley
        valley = 0
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        # find peak
        peak = 0
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]
        max_profit += peak - valley
    return max_profit


print(maxProfit_2([7, 1, 5, 3, 6, 4]))
