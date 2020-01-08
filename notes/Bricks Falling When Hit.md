---
tags: [2020/01/05, leetcode/803, method/union find]
title: Bricks Falling When Hit
created: '2020-01-04T10:29:39.726Z'
modified: '2020-01-04T10:30:52.559Z'
---

# Bricks Falling When Hit

We have a grid of 1s and 0s; the 1s in a cell represent bricks.  A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

Example 1:
Input: 
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
Output: [2]
Explanation: 
If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.
Example 2:
Input: 
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: 
When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.
 

Note:

The number of rows and columns in the grid will be in the range [1, 200].
The number of erasures will not exceed the area of the grid.
It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
An erasure may refer to a location with no brick - if it does, no bricks drop.

## Solution

```python
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        m = len(grid[0])
        
        def index(i, j):
            return i * m + j
        
        def neighbours(i, j):
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < n and 0 <= y < m:
                    yield x, y
        
        uf = UF(n*m+1)
        A = [row[:] for row in grid]
        for i, j in hits:
            A[i][j] = 0
        
        for i, row in enumerate(A):
            for j, v in enumerate(row):
                if not v: continue
                idx = index(i, j)
                if i == 0:
                    uf.union(idx, n*m)
                
                if i and A[i-1][j]:
                    uf.union(idx, index(i-1, j))
                
                if j and A[i][j-1]:
                    uf.union(idx, index(i, j-1))
        
        res = []
        for i, j in reversed(hits):
            pre_top_cnt = uf.top_cnt()
            if grid[i][j] == 0:
                res.append(0)
            else:
                idx = index(i, j)
                for ni, nj in neighbours(i, j):
                    if A[ni][nj]:
                        uf.union(idx, index(ni, nj))
                if i == 0:
                    uf.union(idx, n*m)
                A[i][j] = 1
                res.append(max(0, uf.top_cnt() - pre_top_cnt - 1))
        return res[::-1]
    
class UF(object):
    
    def __init__(self, n):
        self.parents = range(n)
        self.ranks = [0] * n
        self.sizes = [1] * n
    
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def union(self, p, q):
        u = self.find(p)
        v = self.find(q)
        if u == v:
            return
        
        if self.ranks[u] < self.ranks[v]:
            self.parents[u] = v
            self.sizes[v] += self.sizes[u]
        elif self.ranks[v] < self.ranks[u]:
            self.parents[v] = u
            self.sizes[u] += self.sizes[v]
        else:
            self.parents[u] = v
            self.ranks[v] += 1
            self.sizes[v] += self.sizes[u]
            
    def size(self, p):
        return self.sizes[self.find(p)]
    
    def top_cnt(self):
        return self.size(len(self.sizes)-1)-1
        
        
```

## schedule

* [x] 2020/01/04
* [ ] 2020/01/05

## refs

* [lc](https://leetcode.com/problems/bricks-falling-when-hit/)
