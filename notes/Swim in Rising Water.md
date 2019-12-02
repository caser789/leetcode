---
tags: [2019/11/11, leetcode/778]
title: Swim in Rising Water
created: '2019-10-13T11:08:26.230Z'
modified: '2019-10-27T04:55:03.334Z'
---

# Swim in Rising Water

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

### Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

### Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

## Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].


## Solution

```python
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        pq = MinPriorityQueue()
        seen = [[False]*n for _ in range(n)]
        res = 0
        pq.push((grid[0][0], 0, 0))
        while True:
            t, x, y = pq.pop()
            res = max(res, t)
            if x == y == n - 1:
                return res
            seen[x][y] = True
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < n and 0 <= j < n and not seen[i][j]:
                    pq.push((grid[i][j], i, j))


class MinPriorityQueue(object):
    def __init__(self):
        self.keys = [None] * 2
        self.n = 0

    def __len__(self):
        """
        >>> q = MinPriorityQueue()
        >>> len(q)
        0
        >>> q.push(3)
        >>> q.push(2)
        >>> q.push(1)
        >>> len(q)
        3
        >>> q.pop()
        1
        >>> len(q)
        2
        """
        return self.n

    def push(self, v):
        """
        >>> q = MinPriorityQueue()
        >>> q.push(3)
        >>> q.min
        3
        >>> q.push(2)
        >>> q.min
        2
        >>> q.push(1)
        >>> q.min
        1
        """
        if self.n + 1 == len(self.keys):
            self._resize(2*len(self.keys))

        self.n += 1
        self.keys[self.n] = v
        self._swim(self.n)

    def pop(self):
        """
        >>> q = MinPriorityQueue()
        >>> q.push(1)
        >>> q.push(3)
        >>> q.push(2)
        >>> q.pop()
        1
        >>> q.keys
        [None, 2, 3, None]
        >>> q.pop()
        2
        >>> q.pop()
        3
        >>> q.pop()
        Traceback (most recent call last):
            ...
        IndexError: underflow
        """
        if not self.n:
            raise IndexError('underflow')

        keys = self.keys
        res = keys[1]
        keys[1], keys[self.n] = keys[self.n], keys[1]
        keys[self.n] = None
        self.n -= 1

        self._sink(1)

        if self.n and self.n * 4 == len(self.keys)-1:
            self._resize(len(self.keys)/2)
        return res

    @property
    def min(self):
        """
        >>> q = MinPriorityQueue()
        >>> q.min
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 4, 1, 2]
        >>> q.n = 3
        >>> q.min
        4
        """
        if not self.n:
            raise IndexError('underflow')
        return self.keys[1]

    def _swim(self, n):
        """
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 2, 3, None, 1]
        >>> q.n = 4
        >>> q._swim(4)
        >>> q.keys
        [None, 1, 2, None, 3]
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 3, 2, None, 1]
        >>> q.n = 4
        >>> q._swim(4)
        >>> q.keys
        [None, 1, 3, None, 2]
        """
        keys = self.keys
        while n > 1 and keys[n/2] > keys[n]:
            keys[n/2], keys[n] = keys[n], keys[n/2]
            n /= 2

    def _sink(self, n):
        """
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 3, 2, 1]
        >>> q.n = 3
        >>> q._sink(1)
        >>> q.keys
        [None, 1, 2, 3]
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 3, 1, 2]
        >>> q.n = 3
        >>> q._sink(1)
        >>> q.keys
        [None, 1, 3, 2]
        """
        keys = self.keys
        while 2 * n <= self.n:
            i = 2 * n
            if i < self.n and keys[i+1] < keys[i]:
                i += 1

            if keys[i] >= keys[n]:
                break

            keys[i], keys[n] = keys[n], keys[i]
            n = i

    def _resize(self, n):
        """
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 1, 2, 3]
        >>> q.n = 3
        >>> q._resize(6)
        >>> q.keys
        [None, 1, 2, 3, None, None]
        """
        tmp = [None]*n
        for i in range(self.n+1):
            tmp[i] = self.keys[i]
        self.keys = tmp

```

```python
import heapq
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        heap = []
        
        heapq.heappush(heap, (grid[0][0], 0, 0))
        
        res = 0
        seen = [[False] * n for _ in range(n)]
        while True:
            v, x, y = heapq.heappop(heap)
            res = max(res, v)
            seen[x][y] = True
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < n and 0 <= j < n and not seen[i][j]:
                    heapq.heappush(heap, (grid[i][j], i, j))
            if x == y == n - 1:
                return res        
```

## schedule

* [x] 0 2019/10/13
* [x] 1 2019/10/14
* [x] 1 2019/10/17
* [x] 1 2019/10/20
* [x] 1 2019/10/27
* [ ] 1 2019/11/11
