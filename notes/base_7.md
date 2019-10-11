---
tags: [2019/10/25, application/divmod, leetcode/504]
title: Base 7
created: '2019-09-24T15:16:26.061Z'
modified: '2019-10-10T11:58:44.902Z'
---

# Base 7

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].

## Solution

```python
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            neg = True
            num = -num
        else:
            neg = False
        
        res = []
        while num:
            num, c = divmod(num, 7)
            res.append(str(c))
        
        if neg:
            res.append('-')
        
        return ''.join(res[::-1])
        
```

## schedule

* [x] 0 2019/09/29
* [x] 1 2019/09/30
* [x] 1 2019/10/03
* [x] 1 2019/10/10
* [ ] 1 2019/10/25
