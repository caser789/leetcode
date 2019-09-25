---
tags: [2019/10/10, leetcode/204, math/prime]
title: Count Primes
created: '2019-09-07T09:02:06.394Z'
modified: '2019-09-25T04:50:06.294Z'
---

# Count Primes

Count the number of prime numbers less than a non-negative number, n.

### Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

## Solution

```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        lst = [True] * n
        lst[0] = False
        lst[1] = False
        i = 2
        while i < n:
            if lst[i]:
                j = 2
                while j * i < n:
                    lst[j*i] = False
                    j += 1

            i += 1
        return sum(1 for i in lst if i)
```

## schedule

* [x] 0 2019/09/14
* [x] 1 2019/09/15
* [x] 1 2019/09/18
* [x] 1 2019/09/25
* [ ] 1 2019/10/10
