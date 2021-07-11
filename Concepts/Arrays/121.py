'''

121. Best time to buy and sell stocks

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0

'''

def maxProfit(prices):
  min_price = float('inf')
  max_price = float('-inf')
  for i in range(len(prices)):
    print('prices[i] is ', prices[i], 'and min_price is', min_price, 'and max_price is', max_price)
    if prices[i] < min_price:
      min_price = prices[i]
    elif prices[i] - min_price > max_price:
      max_price = prices[i] - min_price
  return max_price if max_price > 0 else 0

# maxProfitExam([7,1,5,3,6,4])
