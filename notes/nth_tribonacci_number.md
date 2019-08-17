---
tags: [2019/08/17, leetcode/1137, method/dp]
title: N-th Tribonacci Number
created: '2019-08-17T09:34:38.432Z'
modified: '2019-08-17T09:35:17.963Z'
---

# N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows:

```
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
```

Given n, return the value of Tn.

### Example 1:

```
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

### Example 2:

```
Input: n = 25
Output: 1389537


Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
```

## Solution

```python
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
```
