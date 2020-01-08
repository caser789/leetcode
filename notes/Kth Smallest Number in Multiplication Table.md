---
tags: [2019/10/20, application/matrix/kth, data structure/priority queue, leetcode/668]
title: Kth Smallest Number in Multiplication Table
created: '2019-10-19T07:30:38.200Z'
modified: '2019-12-14T08:57:29.767Z'
---

# Kth Smallest Number in Multiplication Table

Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]

## Solution

### sort

```python
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        res = []
        for i in range(m):
            for j in range(n):
                res.append((i+1)*(j+1))
        
        res.sort()
        return res[k-1]
```

### pq1

```python
import heapq

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        pq = []
        for i in range(m):
            for j in range(n):
                v = (i+1) * (j+1)
                heapq.heappush(pq, -v)
                if len(pq) > k:
                    heapq.heappop(pq)
        return -pq[0]
```

### pq optimized

```python
import heapq

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        pq = []
        for i in range(m):
            heapq.heappush(pq, (i+1, i, 0))
        
        while k > 1 and pq:
            v, i, j = heapq.heappop(pq)
            k -= 1
            if j + 1 < n:
                
                j += 1
                heapq.heappush(pq, ((i+1)*(j+1), i, j))
        return pq[0][0]
                             
```

### binary search

```python
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        lo = 1
        hi = m * n
        
        while lo < hi:
            mi = (lo+hi)/2
            
            cnt = 0
            for i in range(1, m+1):
                cnt += min(n, mi / i)
                
            if cnt < k:
                lo = mi + 1
            else:
                hi = mi
                
        
        return lo
```

## schedule

* [x] 2019/10/19
* [ ] 2019/10/20
