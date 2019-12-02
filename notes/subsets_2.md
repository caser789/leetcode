---
tags: [2019/08/12, leetcode/90, method/backtracking]
title: Subsets II
created: '2019-08-12T05:05:31.290Z'
modified: '2019-11-23T07:59:14.758Z'
---

#  Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

### Example:

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

## Solution

### backtrack

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        tmp = []
        self.backtrack(res, tmp, 0, nums)
        return res

    def backtrack(self, res, tmp, start, nums):
        res.append(tmp)
        if start == len(nums): return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            tmp.append(nums[i])
            self.backtrack(res, tmp[:], i+1, nums)
            tmp.pop()


"""
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
```

### iter

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        seen = set()
        
        for num in nums:
            n = len(res)
            for i in range(n):
                tmp = res[i] + [num]
                key = tuple(tmp)
                if key not in seen:
                    seen.add(key)
                    res.append(tmp)
        return res
                    
```

## refs

* [lc](https://leetcode.com/problems/subsets-ii/)

