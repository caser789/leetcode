---
tags: [leetcode/50, math, method/recursion]
title: 'Pow(x, n)'
created: '2019-08-03T12:49:16.150Z'
modified: '2019-08-13T15:33:20.109Z'
---

# Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

### Example 1:


```
Input: 2.00000, 10
Output: 1024.00000
```

### Example 2:

```
Input: 2.10000, 3
Output: 9.26100
```

### Example 3:


```
Input: 2.00000, -2
Output: 0.25000
Explanation: 2**-2 = 1/2**2 = 1/4 = 0.25
```


> -100.0 < x < 100.0
> n is a 32-bit signed integer, within the range [−231, 231 − 1]


## Solution


```python
class Solution(object):
    def myPow(self, x, n):
        """
        >>> Solution().myPow(2.0, 10)
        1024.00000
        >>> Solution().myPow(2.1, 3)
        9.26100
        >>> Solution().myPow(2.0, -2)
        0.25000
        """
        if not n:
            return 1

        if n < 0:
            return 1/self.myPow(x, -n)

        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
```
