---
tags: [binary search/1, math]
title: Sqrt(x)
created: '2019-08-02T05:43:22.497Z'
modified: '2019-08-03T04:57:44.758Z'
---

# Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

### Example 1:

```
Input: 4
Output: 2
```

### Example 2:

```
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
```

## Solution

```python
class Solution(object):
    def mySqrt(self, x):
        """
        >>> Solution().mySqrt(4)
        2
        >>> Solution().mySqrt(8)
        2
        >>> Solution().mySqrt(0)
        0
        >>> Solution().mySqrt(1)
        1
        """
        lo = 0
        hi = x
        while lo <= hi:
            mi = (lo+hi) / 2
            v = mi * mi
            if v == x:
                return mi
            elif v < x:
                lo = mi + 1
            else:
                hi = mi - 1
        return hi
```
