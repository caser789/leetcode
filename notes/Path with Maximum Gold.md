---
tags: [2019/11/16, application/best_path, leetcode/1219, method/backtrack]
title: Path with Maximum Gold
created: '2019-11-16T03:30:22.646Z'
modified: '2019-11-25T02:12:30.704Z'
---

# Path with Maximum Gold

In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.


## Solution

### set

```python
class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        self.res = 0
        def collect(i, j, seen, tmp):
            self.res = max(self.res, sum(tmp))
            
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and (x, y)  not in seen and grid[x][y]:
                    seen.add((x, y))
                    tmp.append(grid[x][y])
                    
                    collect(x, y, seen, tmp)
                    
                    tmp.pop()
                    seen.remove((x, y))
        
        seen = set()
        tmp = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    
                    seen.add((i, j))
                    tmp.append(grid[i][j])
                    collect(i, j, seen, tmp)
                    tmp.pop()
                    seen.remove((i, j))
        
        return self.res
        
```

### no set

```python
class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        self.res = 0
        
        def collect(i, j, tmp):

            v = grid[i][j]
            grid[i][j] = '#'
            tmp.append(v)
            self.res = max(self.res, sum(tmp))
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] and grid[x][y] != '#':
                    
                    
                    collect(x, y, tmp)
            tmp.pop()
                
            grid[i][j] = v
        
        tmp = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    collect(i, j, tmp)
        
        return self.res
                    
```

## refs

* [lc](https://leetcode.com/problems/path-with-maximum-gold/)

