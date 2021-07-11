"""
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.


Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
"""

class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1

        if not coins or len(coins) == 0:
            return 0
        
        cache = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        def rec_helper(remaining, idx):
            nonlocal cache

            if idx == len(coins):
               return 0
            
            if remaining == 0:
                return 1

            if cache[idx][remaining] != -1:
                return cache[idx][remaining]
            
            s1 = 0
            if coins[idx] <= remaining:
                s1 = rec_helper(remaining - coins[idx], idx) # pick a coin
            s2 = rec_helper(remaining, idx + 1)

            cache[idx][remaining] = s1 + s2
            return cache[idx][remaining]

        r = rec_helper(amount, 0)
        return r

class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


s = Solution()
print(s.change(100, [1, 101, 102, 103]))
