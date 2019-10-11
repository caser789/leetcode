---
tags: [2019/10/21, leetcode/762]
title: Prime Number of Set Bits in Binary Representation
created: '2019-09-22T11:25:12.804Z'
modified: '2019-10-08T04:48:41.143Z'
---

# Prime Number of Set Bits in Binary Representation

Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

### Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)

### Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)

## Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.

## Solution

```python
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        s = []
        for i in range(L, R+1):
            cnt = 0
            for j in range(32):
                if (i >> j) & 1:
                    cnt += 1
            s.append(cnt)
        
        m = max(s)
        
        primes = [True] * (m+1)
        primes[0] = False
        primes[1] = False
        for i in range(2, m+1):
            j = 2
            while j * i < m + 1:
                primes[j*i] = False
                j += 1
        
        res = 0
        for i in s:
            if primes[i]:
                res += 1
        return res
```

## schedule

* [x] 0 2019/09/25
* [x] 1 2019/09/26
* [x] 1 2019/09/29
* [x] 1 2019/10/06
* [ ] 1 2019/10/21
