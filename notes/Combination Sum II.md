---
tags: [2019/11/15, application/combination, leetcode/40, method/backtrack]
title: Combination Sum II
created: '2019-11-15T05:11:35.991Z'
modified: '2019-11-23T10:15:04.165Z'
---

# Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

## Solution

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = [c for c in candidates if c <= target]
        n = len(candidates)
        res = set()
        candidates.sort()

        def collect(seen, tmp, i):
            if sum(tmp) > target:
                return

            if sum(tmp) == target:
                res.add(tuple(tmp))
                return

            for j in range(i, n):
                if j in seen:
                    continue
                seen.add(j)
                tmp.append(candidates[j])

                collect(seen, tmp, j+1)

                tmp.pop()
                seen.remove(j)

        seen = set()
        tmp = []
        collect(seen, tmp, 0)
        return [list(e) for e in res]
        
```

### better

```python
class Solution(object):
    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        
        def find(tmp, i, s):
            if s < 0:
                return
            if s == 0:
                res.append(tmp[:])
                return
            
            
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]: continue
                tmp.append(nums[j])
                find(tmp, j+1, s-nums[j])
                tmp.pop()
        
        
        find([], 0, target)
        return res
```

## refs

* [lc](https://leetcode.com/problems/combination-sum-ii/)


