---
title: Number of Islands
created: '2019-08-05T05:51:48.433Z'
modified: '2019-08-05T05:52:00.994Z'
---

# Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Example 1:

```
Input:
11110
11010
11000
00000

Output: 1
```

### Example 2:

```
Input:
11000
11000
00100
00011

Output: 3
```

## Solution

* DFS

```python
class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    self.bfs_mark(grid, i, j)
        return cnt


    def bfs_mark(self, grid, i, j):
        grid[i][j] = '#'
        if i - 1 >= 0 and grid[i-1][j] == '1':
            self.bfs_mark(grid, i - 1, j)
        if i + 1 < len(grid) and grid[i+1][j] == '1':
            self.bfs_mark(grid, i + 1, j)
        if j - 1 >= 0 and grid[i][j-1] == '1':
            self.bfs_mark(grid, i, j - 1)
        if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
            self.bfs_mark(grid, i, j + 1)


```
