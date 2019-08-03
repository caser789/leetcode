---
title: Valid Perfect Square
created: '2019-08-03T13:02:02.157Z'
modified: '2019-08-03T13:02:18.333Z'
---

# Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

### Example 1:

```
Input: 16
Output: true
```

### Example 2:

```
Input: 14
Output: false
```

## Solution

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        >>> Solution().isPerfectSquare(16)
        True
        >>> Solution().isPerfectSquare(14)
        False
        >>> Solution().isPerfectSquare(900)
        True
        """
        if num in [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
            return True
        lo = 11
        hi = num / 2
        while lo <= hi:
            mi = (lo+hi)/2
            v = mi * mi
            if v == num:
                return True
            elif v < num:
                lo = mi + 1
            else:
                hi = mi - 1
        return False
```
