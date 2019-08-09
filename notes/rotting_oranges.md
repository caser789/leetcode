---
tags: [2019/08/07, data structure/queue, data structure/tree, leetcode/994, method/traversal/bfs]
title: Rotting Oranges
created: '2019-08-07T14:40:46.100Z'
modified: '2019-08-09T04:47:04.989Z'
---

# Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


### Example 1:

![pic](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

### Example 2:

```
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

### Example 3:

```
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```



> 1 <= grid.length <= 10
> 1 <= grid[0].length <= 10
> grid[i][j] is only 0, 1, or 2.

## Solution

```python
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if not m:
            return 0

        n = len(grid[0])
        if not n:
            return 0

        q = []
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        step = 0
        while q:
            next_q = []
            for x, y in q:
                for xx, yy in self.get_neighbours(x, y, m, n):
                    if grid[xx][yy] == 0:
                        continue
                    if grid[xx][yy] == 2:
                        continue
                    if grid[xx][yy] == 1:
                        next_q.append((xx, yy))
                        grid[xx][yy] = 2
            q = next_q
            if q:
                step += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return step

    def get_neighbours(self, x, y, m, n):
        if x - 1 >= 0:
            yield x - 1, y
        if x + 1 < m:
            yield x + 1, y
        if y - 1 >= 0:
            yield x, y - 1
        if y + 1 < n:
            yield x, y + 1


```
