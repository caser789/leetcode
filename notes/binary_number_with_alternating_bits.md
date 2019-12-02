---
tags: [2019/11/21, leetcode/693]
title: Binary Number with Alternating Bits
created: '2019-09-22T11:19:00.236Z'
modified: '2019-10-22T15:14:20.913Z'
---

# Binary Number with Alternating Bits

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.

## Solution

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = None
        while n:
            n, c = divmod(n, 2)
            if prev is not None and prev == c:
                return False
            prev = c
        return True
```

## schedule

* [x] 0 2019/09/25
* [x] 1 2019/09/26
* [x] 1 2019/09/29
* [x] 1 2019/10/06
* [x] 1 2019/10/21
* [ ] 1 2019/11/21
