---
tags: [2019/08/12, leetcode/77, method/backtracking]
title: Combinations
created: '2019-08-12T14:24:39.992Z'
modified: '2019-08-12T14:25:15.826Z'
---

# Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

### Example:

```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

## Solution

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = range(1, n+1)
        tmp = []
        self.backtrack(res, k, n, tmp, nums, 0)
        return res

    def backtrack(self, res, k, n, tmp, nums, start):
        if len(tmp) == k:
            res.append(tmp)
            return
        for i in range(start, n):
            tmp.append(nums[i])
            self.backtrack(res, k, n, tmp[:], nums, i+1)
            tmp.pop()

```
