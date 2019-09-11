---
tags: [leetcode/202, loop, number]
title: Happy Number
created: '2019-07-30T15:22:08.469Z'
modified: '2019-09-07T08:43:55.086Z'
---

# Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

### Example:

```
Input: 19
Output: true
Explanation:
    1**2 + 9**2 = 82
    8**2 + 2**2 = 68
    6**2 + 8**2 = 100
    1**2 + 0**2 + 0**2 = 1
```

## Solution

```py
class Solution(object):
    def isHappy(self, n):
        """
        >>> s = Solution()
        >>> s.isHappy(1)
        True
        >>> s.isHappy(2)
        False
        >>> s.isHappy(19)
        True
        """
        m = n
        while True:
            n = self.sum(n)
            m = self.sum(self.sum(m))
            if m == 1 or n == 1:
                return True
            if n == m:
                return False

    def sum(self, n):
        """
        >>> s = Solution()
        >>> s.sum(19)
        82
        >>> s.sum(82)
        68
        >>> s.sum(68)
        100
        >>> s.sum(100)
        1
        >>> s.sum(1)
        1
        """
        s = 0
        while n > 0:
            n, i = divmod(n, 10)
            s += i * i
        return s
```
