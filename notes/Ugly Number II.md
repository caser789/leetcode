---
tags: [2019/12/22, application/ugly-number, leetcode/264]
title: Ugly Number II
created: '2019-12-15T04:39:34.703Z'
modified: '2019-12-21T06:23:57.343Z'
---

# Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

## Solution

```python
import heapq


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [2, 3, 5]
        seen = {1}
        pq = [1]
        for i in range(n-1):
            num = heapq.heappop(pq)
            for p in primes:
                m = num * p
                if m not in seen:
                    seen.add(m)
                    heapq.heappush(pq, m)
        return pq[0]
```

### pointer

```python
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2 = 0
        i3 = 0
        i5 = 0
        res = [1]
        
        for i in range(1, n):
            res.append(min(res[i2]*2, res[i3]*3, res[i5]*5))
            
            if res[i] % 2 == 0:
                i2 += 1
            if res[i] %3 == 0:
                i3 += 1
            if res[i] %5 == 0:
                i5 += 1
        
        return res[-1]
```

## refs

* [lc](https://leetcode.com/problems/ugly-number-ii/)

## schedule

* [x] 2019/12/21
* [ ] 2019/12/22

