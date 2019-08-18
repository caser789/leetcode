---
tags: [2019/08/18, design, leetcode/303]
title: Range Sum Query - Immutable
created: '2019-08-18T10:34:37.163Z'
modified: '2019-08-18T10:35:02.452Z'
---

# Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

### Example:

```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

> You may assume that the array does not change.
> There are many calls to sumRange function.

## Solution

```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = nums[:]
        s = 0
        for i, num in enumerate(nums):
            s += num
            self.sums[i] = s


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i-1]
```
