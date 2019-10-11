---
tags: [2019/10/13, leetcode/405]
title: Convert a Number to Hexadecimal
created: '2019-09-24T15:07:17.730Z'
modified: '2019-10-10T12:08:25.563Z'
---

# Convert a Number to Hexadecimal

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"

## Solution

```python
chars = '0123456789abcdef'
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        res = ''
        for i in range(8):
            j = num & 15
            res = chars[j] + res
            num = num >> 4
        return res.lstrip('0')
        
```

## schedule

* [x] 0 2019/09/28
* [x] 1 2019/09/29
* [x] 1 2019/10/02
* [x] 1 2019/10/09
* [x] 1 2019/10/10
* [ ] 1 2019/10/13
