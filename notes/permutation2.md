---
tags: [2019/08/12, leetcode/47, method/backtracking]
title: Permutations II
created: '2019-08-12T10:32:15.263Z'
modified: '2019-08-12T10:33:04.851Z'
---

# Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

### Example:

```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

## Solution

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = {}
        for num in num:
            counter.setdefault(num, 0)
            counter[num] += 1

        res = []
        tmp = []
        self.backtrack(res, tmp, counter, nums)
        return res

    def backtrack(self, res, tmp, counter, nums):
        if len(nums) == len(tmp):
            res.append(tmp)
            return
        for k in counter:
            if counter[k] > 0:
                tmp.append(k)
                counter[k] -= 1
                self.backtrack(res, tmp[:], counter, nums)
                tmp.pop()
                counter[k] += 1
```
