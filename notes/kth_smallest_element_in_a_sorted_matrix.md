---
tags: [2019/10/20, data structure/priority queue, leetcode/378]
title: Kth Smallest Element in a Sorted Matrix
created: '2019-08-19T13:40:29.695Z'
modified: '2019-10-25T01:04:46.121Z'
---

# Kth Smallest Element in a Sorted Matrix


Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

### Example:

```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```

> You may assume k is always valid, 1 ≤ k ≤ n2.

## Solution

### priority queue

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        pq = MinPriorityQueue()
        for c in range(m):
            pq.push((matrix[0][c], 0, c))

        for i in range(k-1):
            v, x, y = pq.pop()
            if x == m - 1:
                continue
            pq.push((matrix[x+1][y], x+1, y))
        return pq.pop()[0]


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

### binary search

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        lo = matrix[0][0]
        hi = matrix[m-1][m-1] + 1
        while lo < hi:
            mi = (lo+hi)/2
            j = m - 1
            cnt = 0
            for i in range(m):
                while j >= 0 and matrix[i][j] > mi:
                    j -= 1
                cnt += j + 1
            if cnt < k:
                lo = mi + 1
            else:
                hi = mi
        return lo
```

### sort

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        values = []
        n = 0
        for row in matrix:
            for val in row:
                values.append(val)
                n += 1


        values.sort()
        return values[k-1] 

```

### pq

```
import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        pq = []
        for row in matrix:
            for val in row:
                heapq.heappush(pq, -val)
                if len(pq) > k:
                    
                
                        heapq.heappop(pq)
                        
        return -pq[0]

```

### better pq

```python
import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        pq = []
        for i in range(n):
            heapq.heappush(pq, (matrix[i][0], i, 0))

        for i in range(k-1):
            v, x, y = heapq.heappop(pq)
            if y + 1 < n:
                heapq.heappush(pq, (matrix[x][y+1], x, y+1))
        return pq[0][0]

```

## refs

* https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code

* https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378

## schedule

* [x] 2019/10/19
* [x] 2019/10/20
* [ ] 2019/10/25
