---
tags: [2019/10/01, leetcode/665]
title: Non-decreasing Array
created: '2019-08-31T08:37:45.110Z'
modified: '2019-09-24T15:25:40.204Z'
---

# Non-decreasing Array

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

### Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

### Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

> The n belongs to [1, 10,000].

## Solution

```python
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
```
