---
tags: [2020/01/02, leetcode/200, method/traversal/dfs, method/union find]
title: Number of Islands
created: '2019-08-05T05:51:48.433Z'
modified: '2020-01-01T14:17:41.424Z'
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


### UF


```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        if not n: return 0
        uf = UF(m*n+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    uf.union(m*n, i*n+j)
                else:
                    for x, y in self.neighbours(i, j, m, n):
                        if grid[x][y] == '1':
                            uf.union(i*n+j, x*n+y)
        return uf.n-1


    def neighbours(self, i, j, m, n):
        if i - 1 >= 0:
            yield i - 1, j
        if i + 1 < m:
            yield i + 1, j
        if j - 1 >= 0:
            yield i, j - 1
        if j + 1 < n:
            yield i, j + 1


class UF(object):

    def __init__(self, n):
        self.n = n
        self.parents = range(n)
        self.size =  [0] * n

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent == q_parent: return

        if self.size[p_parent] < self.size[q_parent]:
            self.parents[p_parent] = q_parent
        elif self.size[q_parent] < self.size[p_parent]:
            self.parents[q_parent] = p_parent
        else:
            self.parents[q_parent] = p_parent
            self.size[p_parent] += 1
        self.n -= 1

lst = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print Solution().numIslands(lst)
```

## schedule 

* [x] 2020/01/01
* [ ] 2020/01/02

## refs

* [lc](https://leetcode.com/problems/number-of-islands/)
