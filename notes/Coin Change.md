---
tags: [2019/11/04, leetcode/322]
title: Coin Change
created: '2019-11-03T06:00:29.513Z'
modified: '2019-11-05T15:19:32.324Z'
---

# Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.


## Solution

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        
        
        """
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        
        n = len(coins)
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            last_cnt = float('inf')
            
            for coin in coins:
                if i - coin >= 0:
                    last_cnt = min(dp[i-coin], last_cnt)
            
            last_cnt += 1
            
            if dp[i] > last_cnt:
                dp[i] = last_cnt
        
        return dp[amount] if dp[amount] != float('inf') else -1
            
            

                
        
        
```

### up-down

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        f(11) = min(1 + f(10), 1+f(9), 1+f(6))
        """
        cache = {0: 0}
        
        def change(amt):
            if amt in cache:
                return cache[amt]
            
            if amt < 0:
                cache[amt] = -1
                return -1
            
            res = float('inf')
            
            for coin in coins:
                x = change(amt-coin)
                if x < 0: continue
                    
                res = min(res, x+1)
            j = -1 if res == float('inf') else res
            cache[amt] = j
            return j
        
        return change(amount)
```

### bottom-up

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        dp = [-1] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            if dp[i] == -1: continue
            for coin in coins:
                j = i + coin
                if j > amount: continue
                if dp[j] == -1 or dp[j] > dp[i] + 1:
                    dp[j] = dp[i] + 1
        
        return dp[-1]
```

## schedule

* [x] 2019/11/03
* [ ] 2019/11/04

## refs

* [lc](https://leetcode.com/problems/coin-change/)


