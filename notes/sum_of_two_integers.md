---
tags: [2019/10/12, leetcode/371]
title: Sum of Two Integers
created: '2019-09-24T15:04:50.751Z'
modified: '2019-10-07T05:16:01.090Z'
---

# Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

## Solution

```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0: return b
        if b == 0: return a
        mask = 0xffffffff
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        if (a >> 31) & 1:
            return ~(a ^ mask)
        return a
        
```

## schedule

* [x] 0 2019/09/27
* [x] 1 2019/09/28
* [x] 1 2019/10/01
* [x] 1 2019/10/02
* [x] 1 2019/10/05
* [ ] 1 2019/10/12
