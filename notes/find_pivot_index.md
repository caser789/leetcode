---
tags: [2019/08/29, leetcode/724, method/math]
title: Find Pivot Index
created: '2019-08-29T15:28:22.382Z'
modified: '2019-08-29T15:37:11.833Z'
---

#  Find Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

### Example 1:

```
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
```

### Example 2:

```
Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
```

> The length of nums will be in the range [0, 10000].
> Each element nums[i] will be an integer in the range [-1000, 1000].

## Solution

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        a = 0
        for i, num in enumerate(nums):
            if a * 2 + num == s:
                return i
            a += num
        return -1
```
