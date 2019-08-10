---
tags: [2019/08/10, data structure/stack, leetcode/739]
title: Daily Temperatures
created: '2019-08-10T07:35:03.404Z'
modified: '2019-08-10T08:01:06.410Z'
---

# Daily Temperatures


Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

> The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

## Solution

```python
class Solution(object):
    def dailyTemperatures(self, T):
        """
        >>> T = [73, 74, 75, 71, 69, 72, 76, 73]
        >>> Solution().dailyTemperatures(T)
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> T = [89,62,70,58,47,47,46,76,100,70]
        >>> Solution().dailyTemperatures(T)
        [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
        """
        res = [0 for _ in T]
        stack = []
        for i, num in enumerate(T):
            while stack and stack[-1][0] < num:
                n, j = stack.pop()
                res[j] = i - j
            stack.append((num, i))
        return res
```
