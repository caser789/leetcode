---
tags: [2019/08/21, leetcode/767]
title: Reorganize String
created: '2019-08-21T14:21:49.569Z'
modified: '2019-08-21T14:22:14.672Z'
---

# Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

### Example 1:

```
Input: S = "aab"
Output: "aba"
```

### Example 2:

```
Input: S = "aaab"
Output: ""
```

> S will consist of lowercase letters and have length in range [1, 500].


## Solution

### Intuitive

```python
class Solution(object):
    def reorganizeString(self, s):
        """
        :type S: str
        :rtype: str
        """
        c_to_cnt = {}
        n = 0
        for c in s:
            c_to_cnt.setdefault(c, 0)
            c_to_cnt[c] += 1
            n += 1

        if not n:
            return ''

        items = c_to_cnt.items()
        items.sort(key=lambda x: -x[1])
        if items[0][1] > (n+1)/2:
            return ''

        lst = []
        for c, cnt in items:
            for i in range(cnt):
                lst.append(c)
        res = [None] * n
        res[::2], res[1::2] = lst[:(n+1)/2], lst[(n+1)/2:]
        return ''.join(res)
```

### heap

```python
class Solution(object):
    def reorganizeString(self, s):
        """
        :type S: str
        :rtype: str
        """
        c_to_cnt = {}
        n = 0
        max_cnt = 0
        for c in s:
            c_to_cnt.setdefault(c, 0)
            c_to_cnt[c] += 1
            max_cnt = max(max_cnt, c_to_cnt[c])
            n += 1
        if max_cnt > (n+1)/2:
            return ''
        pq = MaxPriorityQueue()
        for c, cnt in c_to_cnt.items():
            pq.push((cnt, c))

        res = []
        while len(pq) >= 2:
            cnt1, c1 = pq.pop()
            cnt2, c2 = pq.pop()
            res.extend([c1, c2])

            if cnt1 > 1:
                pq.push((cnt1-1, c1))

            if cnt2 > 1:
                pq.push((cnt2-1, c2))

        if pq:
            res.append(pq.pop()[1])
        return ''.join(res)


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


