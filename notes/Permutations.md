---
tags: [2019/08/12, application/permutation, leetcode/46, method/backtracking]
title: Permutations
created: '2019-08-12T05:40:55.806Z'
modified: '2019-11-24T09:11:59.395Z'
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

### backtrack

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def search(seen, tmp, cnt):
            if cnt == 0:
                res.append(tmp[:])
                return
            
            for num in nums:
                if num in seen: continue
                tmp.append(num)
                seen.add(num)
                search(seen, tmp, cnt-1)
                tmp.pop()
                seen.remove(num)
        
        search(set(), [], len(nums))
        return res
```

## refs

* [lc](https://leetcode.com/problems/permutations/)

