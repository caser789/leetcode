---
tags: [2019/08/30, leetcode/941]
title: Valid Mountain Array
created: '2019-08-30T14:50:55.201Z'
modified: '2019-08-30T14:52:11.460Z'
---

# Valid Mountain Array


Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]


### Example 1:

Input: [2,1]
Output: false

### Example 2:

Input: [3,5,5]
Output: false

### Example 3:

Input: [0,3,2,1]
Output: true


> 0 <= A.length <= 10000
> 0 <= A[i] <= 10000

## Solution

```python
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

```
