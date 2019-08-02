---
tags: [hash, n-sum]
title: 4Sum II
created: '2019-08-01T05:46:15.423Z'
modified: '2019-08-02T05:33:04.746Z'
---

# 4Sum II

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

### Example:

```
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
    The two tuples are:
        1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
        2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
```

## Solution

```python
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        >>> A = [1, 2]
        >>> B = [-2, -1]
        >>> C = [-1, 2]
        >>> D = [0, 2]
        >>> Solution().fourSumCount(A, B, C, D)
        2
        """
        s = {}
        for i in A:
            for j in B:
                k = i + j
                s.setdefault(k, 0)
                s[k] += 1

        res = 0
        for i in C:
            for j in D:
                k = -(i+j)
                if k not in s:
                    continue
                res += s[k]
        return res
```
