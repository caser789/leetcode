---
tags: [2019/10/23, bit, leetcode/231]
title: Power of Two
created: '2019-09-24T15:00:13.612Z'
modified: '2019-10-08T05:22:24.200Z'
---

# Power of Two

Given an integer, write a function to determine if it is a power of two.

### Example 1:

Input: 1
Output: true 
Explanation: 20 = 1

### Example 2:

Input: 16
Output: true
Explanation: 24 = 16

### Example 3:

Input: 218
Output: false

## Solution

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        return not n&(n-1)
        
```

## schedule

* [x] 0 2019/09/27
* [x] 1 2019/09/28
* [x] 1 2019/10/01
* [x] 1 2019/10/08
* [ ] 1 2019/10/23
