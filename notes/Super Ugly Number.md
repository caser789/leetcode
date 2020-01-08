---
tags: [2019/12/22, application/ugly-number, data structure/priority queue, leetcode/313]
title: Super Ugly Number
created: '2019-12-14T14:39:00.484Z'
modified: '2019-12-21T06:23:33.378Z'
---

# Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

## Solution

```
import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        pq = [1]
        seen = {1}
        for i in range(n-1):
            
            num = heapq.heappop(pq)
            
            for p in primes:
                i = p * num
                if i not in seen:
                    heapq.heappush(pq, i)
                    seen.add(i)
        
        return pq[0]
```


### pointers

```python
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        
        res = [1]
        m = len(primes)
        indexes = [0] * m
        
        for i in range(1, n):
            res.append(min(res[index] * prime for index, prime in zip(indexes, primes)))
            
            for j in range(m):
                if res[i] % primes[j] == 0:
                    indexes[j] += 1
        
        return res[-1]
```

## refs

* [lc](https://leetcode.com/problems/super-ugly-number/)


## schedule

* [x] 2019/12/21
* [ ] 2019/12/22
