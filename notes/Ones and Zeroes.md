---
tags: [2019/11/06, leetcode/474]
title: Ones and Zeroes
created: '2019-11-06T01:33:57.481Z'
modified: '2019-11-07T01:24:36.564Z'
---

# Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
 

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
 

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

## Solution

### brute force

```python
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        f(i, m, n) = max(f(i-1, m, n) + f(i-1, m-x, n-y))
        """
        
        
        return self.find(strs, m, n, len(strs)-1)
    
    def find(self, strs, m, n, i):
        if i < 0:
            return 0

        
        x = self.find(strs, m, n, i-1)
        
        s = strs[i]
        count_0 = s.count('0')
        count_1 = len(s) - count_0
        
        y = 0
        if count_0 <= m and count_1 <= n:
            y = self.find(strs, m-count_0, n-count_1, i-1) + 1
            
        return max(y, x)
        
            
```

### DP top-down

```python
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        f(i, m, n) = max(f(i-1, m, n) + f(i-1, m-x, n-y))
        """
        
        d = {}
        return self.find(strs, m, n, len(strs)-1, d)
    
    def find(self, strs, m, n, i, cache):
        if i < 0:
            return 0

        if (m, n, i) in cache:
            return cache[(m, n, i)]
        
        x = self.find(strs, m, n, i-1, cache)
        
        s = strs[i]
        count_0 = s.count('0')
        count_1 = len(s) - count_0
        
        y = 0
        if count_0 <= m and count_1 <= n:
            y = self.find(strs, m-count_0, n-count_1, i-1, cache) + 1
        
        
        cache[(m, n, i)] = max(y, x)
        return cache[(m, n, i)]
        
            
```

### dp bottom-up

```python
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        f(i, m, n) = max(f(i-1, m, n), f(i-1, m-x, n-y)+1)
        """
        t = len(strs)
        
        dp = [[[0]*(n+1) for j in range(m+1)] for i in range(t+1)]
        
        for i in range(1, t+1):           
            s = strs[i-1]
            x = s.count('0')
            y = len(s) - x
            
            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j >= x and k >= y:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-x][k-y]+1)
        
        return dp[-1][-1][-1]
                        
```

## refs

* [lc](https://leetcode.com/problems/ones-and-zeroes/)

