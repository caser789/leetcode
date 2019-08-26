---
tags: [2019/08/26, leetcode/977, method/sort/merge]
title: Squares of a Sorted Array
created: '2019-08-26T15:07:10.033Z'
modified: '2019-08-26T15:34:46.499Z'
---

# Squares of a Sorted Array


Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.


### Example 1:

```
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

### Example 2:

```
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

> 1 <= A.length <= 10000
> -10000 <= A[i] <= 10000
> A is sorted in non-decreasing order.

## Solution


```python
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        j = 0
        while j < n and nums[j] < 0:
            j += 1
        i = j - 1
        res = []

        while i >= 0 and j < n:
            if nums[i]**2 < nums[j]**2:
                res.append(nums[i]**2)
                i -= 1
            else:
                res.append(nums[j]**2)
                j += 1

        while i >= 0:
            res.append(nums[i]**2)
            i -= 1

        while j < n:
            res.append(nums[j]**2)
            j += 1
        return res
```
