---
tags: [2019/08/13, leetcode/70, method/recursion]
title: Climbing Stairs
created: '2019-08-13T15:28:56.433Z'
modified: '2019-08-13T15:29:21.996Z'
---

# Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

### Example 1:

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

### Example 2:

```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Solution

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        store = {0: 0, 1: 1, 2: 2}
        def _climb(n):
            if n in store:
                return store[n]
            res = _climb(n-1) + _climb(n-2)
            store[n] = res
            return res
        return _climb(n)
```
