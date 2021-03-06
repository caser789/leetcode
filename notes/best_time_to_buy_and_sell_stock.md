---
tags: [2019/08/20, leetcode/121]
title: Best Time to Buy and Sell Stock
created: '2019-08-20T14:13:58.258Z'
modified: '2019-08-20T14:14:23.251Z'
---

# Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

### Example 1:

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

### Example 2:

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Solution

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        profit = 0
        lo = prices[0]
        for i in range(1, n):
            if prices[i] < lo:
                lo = prices[i]
            elif prices[i] - lo > profit:
                profit = prices[i] - lo
        return profit
```
