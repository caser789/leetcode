---
tags: [2019/08/18, leetcode/363, TODO]
title: Max Sum of Rectangle No Larger Than K
created: '2019-08-18T14:26:07.077Z'
modified: '2019-08-18T14:26:53.620Z'
---

# Max Sum of Rectangle No Larger Than K

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

### Example:

```
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
```

> The rectangle inside the matrix must have an area > 0.
> What if the number of rows is much larger than the number of columns?

## Solution

```python
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
```
