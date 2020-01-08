---
tags: [2019/08/20, application/array/kth, data structure/priority queue, leetcode/692, method/sort]
title: Top K Frequent Words
created: '2019-08-20T00:54:22.041Z'
modified: '2019-12-14T10:31:03.605Z'
---

# Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

### Example 1:

```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```

### Example 2:

```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```

> You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
> Input words contain only lowercase letters.

## Follow up:

* Try to solve it in O(n log k) time and O(n) extra space.


## Solution

### sort

```python
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        store = {}
        for word in words:
            store.setdefault(word, 0)
            store[word] += 1
        items = store.items()
        items.sort(key=lambda x: (-x[1], x[0]))
        return [items[i][0] for i in range(k)]
```

### heapq

```python
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = {}
        for word in words:
            counter.setdefault(word, 0)
            counter[word] += 1
        
        pq = MinPQ(k+1)
        for word, cnt in counter.items():
            pq.push(word, cnt)
            if len(pq) > k:
                pq.pop()
            
        res = []
        for i in range(k):
            res.append(pq.pop())
        
        return res[::-1]

    
class MinPQ(object):
    def __init__(self, n):
        self.vals = [None] * (n+1)
        self.n = 0
    
    def __len__(self):
        return self.n
    
    def push(self, word, cnt):
        self.n += 1
        self.vals[self.n] = (word, cnt)
        self._swim(self.n)
    
    def pop(self):
        v = self.vals[1]
        self.vals[1] = self.vals[self.n]
        self.n -= 1
        self._sink(1)
        return v[0]
    
    def _swim(self, i):
        while i > 1 and self._compare(i, i/2) < 0 :
            self._swap(i, i/2)
            i /= 2
    
    def _sink(self, i):
        while i*2 <= self.n:
            j = i * 2
            if j + 1 <= self.n and self._compare(j+1, j) < 0:
                j += 1
            if self._compare(i, j) < 0:
                return
            self._swap(i, j)
            i = j
    
    def _compare(self, i, j):
        w1, c1 = self.vals[i]
        w2, c2 = self.vals[j]
        if c1 < c2:
            return -1
        if c1 > c2:
            return 1
        if w1 > w2:
            return -1
        if w1 < w2:
            return 1
        return 0
    
    def _swap(self, i, j):
        self.vals[i], self.vals[j] = self.vals[j], self.vals[i]

```

## refs

* [lc](https://leetcode.com/problems/top-k-frequent-words/)

