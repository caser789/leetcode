---
tags: [2019/10/20, data structure/priority queue, leetcode/786]
title: K-th Smallest Prime Fraction
created: '2019-10-19T09:15:08.831Z'
modified: '2019-10-19T09:58:18.896Z'
---

# K-th Smallest Prime Fraction

A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

### Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]

## Note:

A will have length between 2 and 2000.
Each A[i] will be between 1 and 30000.
K will be between 1 and A.length * (A.length - 1) / 2.

## Solution

### heap

```python
import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        pq = []
        m = n = len(A)
        
        for j in range(m):
            heapq.heappush(pq, (1.0*A[j]/A[n-1-0], 0, j))
        
        for _ in range(K-1):
            v, i, j = heapq.heappop(pq)
            if i + 1 < n:
                i += 1
                heapq.heappush(pq, (1.0*A[j]/A[n-1-i], i, j))
        
        v, i, j = pq[0]
        return [A[j], A[n-1-i]]      
```

### binary search

```python
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        lo = 0
        hi = 1.0
        p = 0
        q = 1

        n = len(A)
        while True:
            p = 0
            cnt = 0
            mi = (lo+hi) / 2.0

            j = n - 1
            for i in range(n):
                while j >= 0 and A[i] > mi * A[n-1-j]:
                    j -= 1
                cnt += j + 1

                if j >= 0 and p * A[n-1-j] < q * A[i]:
                    p = A[i]
                    q = A[n-1-j]

            if cnt < K:
                lo = mi
            elif cnt > K:
                hi = mi
            else:
                return [p, q]

```

## Schedule

* [x] 2019/10/19
* [ ] 2019/10/20
