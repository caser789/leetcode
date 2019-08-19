---
tags: [2019/08/19, leetcode/973]
title: K Closest Points to Origin
created: '2019-08-19T12:46:57.686Z'
modified: '2019-08-19T12:48:29.596Z'
---

# K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

### Example 1:

```
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
```

### Example 2:

```
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
```


> 1 <= K <= points.length <= 10000
> -10000 < points[i][0] < 10000
> -10000 < points[i][1] < 10000

## Solution

```python
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        pq = MaxPriorityQueue()
        for x, y in points:
            d = x*x + y*y
            if len(pq) == K:
                if d < pq.max[0]:
                    pq.pop()
                    pq.push((d, x, y))
            else:
                pq.push((d, x, y))
        res = []
        for _ in range(len(pq)):
            d, x, y = pq.pop()
            res.append([x, y])
        return res



class MaxPriorityQueue(object):

    def __init__(self):
        self.keys = [None] * 2
        self.n = 0

    def __len__(self):
        """
        >>> q = MaxPriorityQueue()
        >>> len(q)
        0
        >>> q.push(1)
        >>> q.push(2)
        >>> q.push(3)
        >>> len(q)
        3
        >>> q.pop()
        3
        >>> len(q)
        2
        """
        return self.n

    def push(self, i):
        """
        >>> q = MaxPriorityQueue()
        >>> q.push(1)
        >>> q.max
        1
        >>> q.push(3)
        >>> q.max
        3
        >>> q.push(2)
        >>> q.max
        3
        """
        if self.n + 1 == len(self.keys):
            self._resize(len(self.keys)*2)

        self.n += 1
        self.keys[self.n] = i
        self._swim(self.n)

    def pop(self):
        """
        >>> q = MaxPriorityQueue()
        >>> q.push(1)
        >>> q.push(3)
        >>> q.push(2)
        >>> q.pop()
        3
        >>> q.pop()
        2
        >>> q.pop()
        1
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

        if self.n and self.n * 4 == len(self.keys) - 1:
            self._resize(len(self.keys)/2)
        return res

    @property
    def max(self):
        """
        >>> q = MaxPriorityQueue()
        >>> q.max
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> q = MaxPriorityQueue()
        >>> q.keys = [None, 1, 2, 3]
        >>> q.n = 3
        >>> q.max
        1
        """
        if not self.n:
            raise IndexError('underflow')
        return self.keys[1]

    def _swim(self, n):
        """
        >>> q = MaxPriorityQueue()
        >>> q.keys = [None, 1, 2, None, 3]
        >>> q.n = 4
        >>> q._swim(4)
        >>> q.keys
        [None, 3, 1, None, 2]
        >>> q = MaxPriorityQueue()
        >>> q.keys = [None, 2, 1, None, 3]
        >>> q.n = 4
        >>> q._swim(4)
        >>> q.keys
        [None, 3, 2, None, 1]
        """
        keys = self.keys
        while n > 1 and keys[n/2] < keys[n]:
            keys[n/2], keys[n] = keys[n], keys[n/2]
            n /= 2

    def _sink(self, n):
        """
        >>> q = MaxPriorityQueue()
        >>> q.keys = [None, 1, 2, 3]
        >>> q.n = 3
        >>> q._sink(1)
        >>> q.keys
        [None, 3, 2, 1]
        >>> q = MaxPriorityQueue()
        >>> q.keys = [None, 2, 1, 3]
        >>> q.n = 3
        >>> q._sink(1)
        >>> q.keys
        [None, 3, 1, 2]
        """
        keys = self.keys
        while 2 * n <= self.n:
            i = 2 * n
            if i < self.n and keys[i+1] > keys[i]:
                i = i + 1

            if keys[i] <= keys[n]:
                break

            keys[n], keys[i] = keys[i], keys[n]
            n = i

    def _resize(self, n):
        """
        >>> # 1. test resize up
        >>> q = MaxPriorityQueue()
        >>> q.keys = [None, 1, 2]
        >>> q.n = 2
        >>> q._resize(6)
        >>> q.keys
        [None, 1, 2, None, None, None]
        >>> # 2. test resize down
        >>> q = MaxPriorityQueue()
        >>> q.keys = [None, 1, 2, None, None, None]
        >>> q.n = 2
        >>> q._resize(3)
        >>> q.keys
        [None, 1, 2]
        """
        tmp = [None] * n
        for i in range(self.n+1):
            tmp[i] = self.keys[i]
        self.keys = tmp
```
