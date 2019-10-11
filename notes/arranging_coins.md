---
tags: [2019/10/24, leetcode/441]
title: Arranging Coins
created: '2019-09-24T15:08:24.658Z'
modified: '2019-10-08T14:28:15.184Z'
---

# Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

## Solution

```python
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        i = 1
        while n >= i:
            
            n -= i
            i += 1
        return i-1
               
```

## schedule

* [x] 0 2019/09/28
* [x] 1 2019/09/29
* [x] 1 2019/10/02
* [x] 1 2019/10/09
* [ ] 1 2019/10/24
