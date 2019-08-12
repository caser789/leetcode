---
tags: [2019/08/12, leetcode/46, method/backtracking]
title: Permutations
created: '2019-08-12T05:40:55.806Z'
modified: '2019-08-12T05:41:30.207Z'
---

# Permutations

Given a collection of distinct integers, return all possible permutations.

### Example:

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## Solution

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        self.backtrack(res, tmp, nums)
        return res

    def backtrack(self, res, tmp, nums):
        if len(tmp) == len(nums):
            res.append(tmp)
        for num in nums:
            if num in tmp: continue
            tmp.append(num)
            self.backtrack(res, tmp[:], nums)
            tmp.pop()


"""
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
```
