---
tags: [2019/11/09, leetcode/64]
title: Minimum Path Sum
created: '2019-11-09T08:00:45.523Z'
modified: '2019-12-02T14:21:03.293Z'
---

# Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

### Example:

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```

Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


## Solution

### brute force

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        f(x, y) = min(f(x-1, y) + v .  f(x, y-1) + 1 + v)
        [
            [1],
        ]
        """
        
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        if not n: return 0
        
        def find(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
                  
            if i - 1 < 0:
                return find(i, j-1) + grid[i][j]
                
            if j - 1 < 0:
                return find(i-1, j) + grid[i][j]
            
            return min(find(i-1, j), find(i, j-1)) + grid[i][j]
        
        
        return find(m-1, n-1)
```

### dp top-down

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        f(x, y) = min(f(x-1, y) + v .  f(x, y-1) + 1 + v)
        [
            [1],
        ]
        """
        
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        if not n: return 0
        
        cache = {}
        
        def find(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            
            key = (i, j)
            if key in cache:
                return cache[key]
                        
            if i - 1 < 0:
                cache[key] = find(i, j-1) + grid[i][j]
                return cache[key]
                
            if j - 1 < 0:
                cache[key] = find(i-1, j) + grid[i][j]
                return cache[key]
            
            cache[key] = min(find(i-1, j), find(i, j-1)) + grid[i][j]
            return cache[key]
        
        
        return find(m-1, n-1)
```

### dp bottom-up

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        if not n: return 0
        
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]
        
        
```

## refs

* [lc](https://leetcode.com/problems/minimum-path-sum/)
