---
tags: [2019/08/13, leetcode/509, method/dp, method/recursion]
title: Fibonacci Number
created: '2019-08-13T15:26:28.429Z'
modified: '2019-08-17T09:11:52.769Z'
---

# Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).


### Example 1:

```
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

### Example 2:

```
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

### Example 3:

```
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```



> 0 ≤ N ≤ 30.

## Solution

### recursion

```python
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        store = {0: 0, 1: 1}
        def _fib(N):
            if N in store:
                return store[N]
            res = _fib(N-1) + _fib(N-2)
            store[N] = res
            return res
        return _fib(N)
```

### dp

```python
class Solution(object):
    def fib(self, n):
        """
        :type N: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

```
