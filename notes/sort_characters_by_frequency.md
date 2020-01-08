---
tags: [2019/08/19, leetcode/451, method/sort/bucket]
title: Sort Characters By Frequency
created: '2019-08-19T13:07:23.672Z'
modified: '2019-12-14T06:48:38.254Z'
---

# Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

### Example 1:

```
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

### Example 2:

```
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
```

### Example 3:

```
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

## Solution

### priority queue

```python
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        store = {}
        for c in s:
            store.setdefault(c, 0)
            store[c] += 1

        pq = MaxPriorityQueue()
        for c, cnt in store.items():
            pq.push((cnt, c))

        res = []
        for _ in range(len(pq)):
            cnt, c = pq.pop()
            res.append(c * cnt)
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

### sort

```python
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        store = {}
        for c in s:
            store.setdefault(c, 0)
            store[c] += 1

        items = store.items()
        items.sort(key=lambda x: -x[1])

        res = []
        for c, cnt in items:
            res.append(c * cnt)
        return ''.join(res)
```

## refs

* [lc](https://leetcode.com/problems/sort-characters-by-frequency/)
* [o n](https://leetcode.com/problems/sort-characters-by-frequency/discuss/93445/O(n)-Easy-to-understand-Java-Solution)
