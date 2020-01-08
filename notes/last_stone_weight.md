---
tags: [2019/08/15, data structure/priority queue, leetcode/1046]
title: Last Stone Weight
created: '2019-08-15T15:13:52.849Z'
modified: '2019-12-14T06:14:51.870Z'
---

# Last Stone Weight

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)


### Example 1:

```
Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
```

> 1 <= stones.length <= 30
> 1 <= stones[i] <= 1000

## Solution

```python
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if not stones:
            return 0

        pq = MaxPriorityQueue()
        for stone in stones:
            pq.push(stone)

        while len(pq) > 1:
            a = pq.pop()
            b = pq.pop()
            s = abs(a-b)
            if s:
                pq.push(s)

        if not pq: return 0
        return pq.pop()


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

### heapq

```python
import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        pq = []
        for s in stones:
            heapq.heappush(pq, -s)
        
        while len(pq) > 1:
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)
            if x != y:
                heapq.heappush(pq, x-y)
        
        if pq:
            return -pq[0]
        return 0
```

## refs

* [lc](https://leetcode.com/problems/last-stone-weight/)
