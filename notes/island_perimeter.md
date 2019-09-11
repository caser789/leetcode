---
tags: [2019/09/14, leetcode/463]
title: Island Perimeter
created: '2019-09-07T08:21:48.277Z'
modified: '2019-09-11T13:54:18.474Z'
---

# Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



### Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

![pic](https://assets.leetcode.com/uploads/2018/10/12/island.png)

## Solution

```python
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        island = 0
        nei = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island += 1
                    if i < n -1 and grid[i+1][j] == 1: nei += 1
                    if j < m-1 and grid[i][j+1] == 1: nei += 1
        return 4 * island - 2 * nei

```


## schedule

* [x] 0 2019/09/10
* [x] 1 2019/09/11
* [ ] 1 2019/09/14
