"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


def coinChange_top_down(coins, amount):
    def helper(coins, remaining_balance, cache):
        if remaining_balance < 0:
            return -1
        if remaining_balance == 0:
            return 0
        if cache[remaining_balance - 1] != 0:  # We have a cache available
            return cache[remaining_balance - 1]

        minimum = float('inf')

        for each_coin in coins:
            res = helper(coins, remaining_balance - each_coin, cache)
            if 0 <= res < minimum:
                minimum = 1 + res

        cache[remaining_balance - 1] = -1 if minimum == float('inf') else minimum
        return cache[remaining_balance - 1]

    cache = [0 for _ in range(amount + 1)]
    return helper(coins, amount, cache)  # since you are not cloning it, recursion still holds the value


def coinChange_bottom_up(coins, amount: int) -> int:
    coins.sort()
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0

    for idx in range(1, amount + 1):
        print('Index ', idx)
        print([i for i in range(amount + 1)])
        for each_coin in coins:
            if each_coin > idx:
                break
            x = idx - each_coin
            # using the curr coin, find out, the min_coins required to get the remaining balance for total of idx
            dp[idx] = min(dp[idx], dp[x] + 1)
            print(each_coin, ' -> ', dp)
            # +1 since we are using each coin used during subtraction
        print('\n\n')
    return dp[-1]


print(coinChange_top_down([1, 2, 5], 11))
print('\n\n\n')
print(coinChange_bottom_up([1, 2, 5], 11))
