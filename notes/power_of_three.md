---
tags: [2019/11/23, bit, leetcode/326]
title: Power of Three
created: '2019-09-24T15:03:04.791Z'
modified: '2019-10-23T05:03:40.705Z'
---

# Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?

## Solution

```python
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1: return False
        
        while n % 3 == 0:
            n /= 3
        
        return n == 1
        
        
```

## schedule

* [x] 0 2019/09/27
* [x] 1 2019/09/28
* [x] 1 2019/10/01
* [x] 1 2019/10/08
* [x] 1 2019/10/23
* [ ] 1 2019/11/23
