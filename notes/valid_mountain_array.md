---
tags: [2019/08/30, leetcode/941, TODO]
title: Valid Mountain Array
created: '2019-08-30T14:50:55.201Z'
modified: '2019-08-30T15:25:22.557Z'
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

### intuitive

```python
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3:
            return False

        increasing = None
        turn = 0
        for i in range(len(A)-1):
            if A[i] == A[i+1]: return False
            if increasing is None and A[i] < A[i+1]:
                increasing = True
            elif increasing is True:
                if turn > 0: return False
                if A[i] > A[i+1]:
                    turn = 1
                    increasing = False
            elif  increasing is False:
                if A[i] < A[i+1]: return False
            else:
                return False
        if turn == 0: return False
        return True
```
