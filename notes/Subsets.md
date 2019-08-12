---
tags: [2019/08/12, leetcode/78, method/backtracking]
title: Subsets
created: '2019-08-12T04:39:24.135Z'
modified: '2019-08-12T04:39:58.691Z'
---

# Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

### Example:

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## Solution

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        self.backtrack(res, tmp, nums, 0)
        return res

    def backtrack(self, res, tmp, nums, start):
        res.append(tmp)
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.backtrack(res, tmp[:], nums, i+1)
            tmp.pop()

"""
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
```
