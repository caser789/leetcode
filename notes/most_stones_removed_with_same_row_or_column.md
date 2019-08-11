---
tags: [2019/08/10, leetcode/947, method/union find]
title: Most Stones Removed with Same Row or Column
created: '2019-08-11T02:23:00.531Z'
modified: '2019-08-11T02:24:07.116Z'
---

# Most Stones Removed with Same Row or Column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

### Example 1:

```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
```

### Example 2:

```
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
```

### Example 3:

```
Input: stones = [[0,0]]
Output: 0
```

> 1 <= stones.length <= 1000
> 0 <= stones[i][j] < 10000

## Solution

### TLE

```python
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        row_to_points = {}
        col_to_points = {}
        max_row = 0
        max_col = 0
        cnt = 0
        s = set()
        for x, y in stones:
            max_row = max(max_row, x)
            max_col = max(max_col, y)
            row_to_points.setdefault(x, [])
            row_to_points[x].append((x, y))
            col_to_points.setdefault(y, [])
            col_to_points[y].append((x, y))
            cnt += 1
            s.add((x, y))
        max_col += 1
        max_row += 1
        uf = UF(max_col*max_row+1)
        for _, points in row_to_points.items():
            first = points[0][0] * max_col + points[0][1]
            for i, j in points[1:]:
                other = i * max_col + j
                uf.union(first, other)
        for _, points in col_to_points.items():
            first = points[0][0] * max_col + points[0][1]
            for i, j in points[1:]:
                other = i * max_col + j
                uf.union(first, other)
        last = max_col * max_row
        for i in range(max_row):
            for j in range(max_col):
                if (i, j) in s: continue
                uf.union(last, i*max_col+j)
        return cnt - uf.n + 1


class UF(object):

    def __init__(self, n):
        self.parents = range(n)
        self.n = n
        self.size = [0] * n

    def union(self, p, q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent == q_parent:
            return
        if self.size[p_parent] < self.size[q_parent]:
            self.parents[p_parent] = q_parent
        elif self.size[q_parent] < self.size[p_parent]:
            self.parents[q_parent] = p_parent
        else:
            self.parents[q_parent] = p_parent
            self.size[p_parent] += 1
        self.n -= 1

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
print Solution().removeStones(stones)
```

### accepted

```python
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        uf = UF(20000)
        for x, y in stones:
            uf.union(x, y+10000)
        return len(stones) - set(uf.find(x) for x, _ in stones)


class UF(object):

    def __init__(self, n):
        self.parents = range(n)
        self.n = n
        self.size = [0] * n

    def union(self, p, q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent == q_parent:
            return
        if self.size[p_parent] < self.size[q_parent]:
            self.parents[p_parent] = q_parent
        elif self.size[q_parent] < self.size[p_parent]:
            self.parents[q_parent] = p_parent
        else:
            self.parents[q_parent] = p_parent
            self.size[p_parent] += 1
        self.n -= 1

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
print Solution().removeStones(stones)
```
