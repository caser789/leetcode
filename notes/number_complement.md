---
tags: [2019/11/25, application/divmod, leetcode/476]
title: Number Complement
created: '2019-09-24T15:12:42.332Z'
modified: '2019-10-25T04:55:35.042Z'
---

# Number Complement

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

## Solution

```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 1
        if num == 1: return 0
        
        res = []
        while num:
            num, c = divmod(num, 2)
            res.append(1-c)
        
        s = 0
        for v in res[::-1]:
            s = s * 2 + v
        return s
```

## schedule

* [x] 0 2019/09/29
* [x] 1 2019/09/30
* [x] 1 2019/10/03
* [x] 1 2019/10/10
* [x] 1 2019/10/25
* [ ] 1 2019/11/25
