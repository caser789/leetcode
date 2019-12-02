---
tags: [2019/11/25, application/best_path, leetcode/980, method/backtrack]
title: Unique Paths III
created: '2019-11-25T05:03:27.823Z'
modified: '2019-11-25T05:06:10.520Z'
---

# Unique Paths III

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20

## Solution

```python
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        res = []
        tmp = []
        self.count = 0
        
        non_ob = m * n
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    non_ob -= 1
        
        def search(i, j):   
            if grid[i][j] == 2:
                if len(tmp) == non_ob:
                    self.count += 1
                return
            
            v = grid[i][j]
            grid[i][j] = '#'
            
            for x, y in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                if 0 <= x < n and 0 <= y < m and (grid[x][y] == 0 or grid[x][y] == 2):
                    tmp.append((x, y))
                    search(x, y)
                    tmp.pop()
                    
            grid[i][j] = v
         
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    tmp.append((i, j))
                    search(i, j)
                    tmp.pop()
        
        return self.count
        
```

### better backtrack


```python
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        
        self.count = 0
        
        non_ob = m * n
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    non_ob -= 1
        
        def search(i, j, k):   
            if grid[i][j] == 2:
                if k == non_ob:
                    self.count += 1
                return
            
            v = grid[i][j]
            grid[i][j] = '#'
            
            for x, y in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                if 0 <= x < n and 0 <= y < m and (grid[x][y] == 0 or grid[x][y] == 2):
                    search(x, y, k+1)    
                    
            grid[i][j] = v
         
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    search(i, j, 1)
        
        return self.count
        
```

## refs

* [lc](https://leetcode.com/problems/unique-paths-iii/)

