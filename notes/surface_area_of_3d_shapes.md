---
tags: [2019/09/25, leetcode/892]
title: Surface Area of 3D Shapes
created: '2019-09-22T11:13:40.302Z'
modified: '2019-09-24T13:55:09.915Z'
---

# Surface Area of 3D Shapes

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

### Example 1:

Input: [[2]]
Output: 10

### Example 2:

Input: [[1,2],[3,4]]
Output: 34

### Example 3:

Input: [[1,0],[0,2]]
Output: 16

### Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

### Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

## Note:

1 <= N <= 50
0 <= grid[i][j] <= 50

## Solution

```python
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        
        res = 0
        
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    res += 2
                    
                    for nr, nc in ((r-1, c), (r+1, c), (r, c+1), (r, c-1)):
                        if 0 <= nr < n and 0 <= nc < m:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        
                        res += max(grid[r][c]-nval, 0)
                        
        return res        
```

## schedule

* [x] 0 2019/09/24
* [ ] 1 2019/09/25
