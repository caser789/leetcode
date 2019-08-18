---
tags: [2019/08/18, leetcode/374, method/search/binary/1]
title: Guess Number Higher or Lower
created: '2019-08-02T05:44:30.312Z'
modified: '2019-08-18T09:34:21.967Z'
---

# Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

    -1 : My number is lower
    1 : My number is higher
    0 : Congrats! You got it!

### Example :

```
Input: n = 10, pick = 6
Output: 6
```

## Solution

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        while lo <= hi:
            mi = (lo + hi) / 2
            v = guess(mi)
            if v == 0:
                return mi
            elif v > 0:
                lo = mi + 1
            else:
                hi = mi - 1
        return hi
```
