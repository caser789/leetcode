---
tags: [2019/08/22, application/array/2-D, leetcode/661]
title: Image Smoother
created: '2019-08-22T13:54:44.757Z'
modified: '2019-08-22T14:05:17.441Z'
---

# Image Smoother


Given a 2D integer matrix M representing the gray scale of an image,
you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.
If a cell has less than 8 surrounding cells, then use as many as you can.

### Example 1:

```
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
```

> The value in the given matrix is in the range of [0, 255].
> The length and width of the given matrix are in the range of [1, 150].

## Solution

```python
class Solution(object):
    def imageSmoother(self, grid):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = self.smooth(grid, i, j, m, n)
        return res

    def smooth(self, grid, i, j, m, n):
        cnt = 0
        s = 0
        if i - 1 >= 0:
            if j - 1 >= 0:
                s += grid[i-1][j-1]
                cnt += 1
            s += grid[i-1][j]
            cnt += 1
            if j + 1 < n:
                s += grid[i-1][j+1]
                cnt += 1

        if j - 1 >= 0:
            s += grid[i][j-1]
            cnt += 1
        s += grid[i][j]
        cnt += 1
        if j + 1 < n:
            s += grid[i][j+1]
            cnt += 1

        if i + 1 < m:
            if j - 1 >= 0:
                s += grid[i+1][j-1]
                cnt += 1
            s += grid[i+1][j]
            cnt += 1
            if j + 1 < n:
                s += grid[i+1][j+1]
                cnt += 1
        return s / cnt
```
