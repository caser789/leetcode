---
tags: [2019/11/11, data structure/priority queue, leetcode/659]
title: Split Array into Consecutive Subsequences
created: '2019-10-13T09:43:21.903Z'
modified: '2019-10-27T06:13:31.849Z'
---

# Split Array into Consecutive Subsequences

Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

### Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

### Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

### Example 3:

Input: [1,2,3,4,4,5]
Output: False
 

Constraints:

1 <= nums.length <= 10000


## Solution

```python
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        interval = [end, -length]
        """
        pq = MinPriorityQueue()
        n = len(nums)
        i = 0
        while i < n:
            if len(pq) == 0:
                pq.push([nums[i], 1])
                i += 1
            elif pq.min[0] == nums[i]:
                pq.push([nums[i], 1])
                i += 1
            elif pq.min[0] + 1 == nums[i]:
                x, y = pq.pop()
                pq.push([nums[i], y+1])
                i += 1
            else:
                x, y = pq.pop()
                if y < 3:
                    return False

        while len(pq):
            x, y = pq.pop()
            if y < 3:
                return False
        return True


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
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        heap = []
        n = len(nums)
        i = 0
        while i < n:
        
            if not heap or nums[i] == heap[0][0]:
                heapq.heappush(heap, [nums[i], 1])
                i += 1
            
            elif nums[i] == heap[0][0] + 1:
                v, cnt = heapq.heappop(heap)
                
                heapq.heappush(heap, [nums[i], cnt+1])
                i += 1
            else:
                v, cnt = heapq.heappop(heap)
                if cnt < 3:
                    return False
        while heap:
            v, cnt = heapq.heappop(heap)
            if cnt < 3:
                return False
            
        return True
                
                
        
```

## schedule

* [x] 0 2019/10/13
* [x] 1 2019/10/14
* [x] 1 2019/10/17
* [x] 1 2019/10/20
* [x] 1 2019/10/27
* [ ] 1 2019/11/11
