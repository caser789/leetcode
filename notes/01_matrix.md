---
tags: [2019/08/10, leetcode/542, TODO]
title: 01 Matrix
created: '2019-08-10T10:28:33.850Z'
modified: '2019-08-10T11:10:26.080Z'
---

# 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

### Example 1:

```
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```

### Example 2:

```
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```


> The number of elements of the given matrix will not exceed 10,000.
> There are at least one 0 in the given matrix.
> The cells are adjacent in only four directions: up, down, left and right.

## Solution

```python
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
```
