---
tags: [2019/11/23, application/ugly-number, leetcode/263]
title: Ugly Number
created: '2019-09-24T15:01:13.034Z'
modified: '2019-12-21T05:37:03.410Z'
---

# Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].

## Solution

```python
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num in [1, 2, 3, 5]:
            return True
        if num % 2 == 0:
            return self.isUgly(num/2)
        if num % 3 == 0:
            return self.isUgly(num/3)
        if num % 5 == 0:
            return self.isUgly(num/5)
        return False
```


## schedule

* [x] 0 2019/09/27
* [x] 1 2019/09/28
* [x] 1 2019/10/01
* [x] 1 2019/10/08
* [x] 1 2019/10/23
* [ ] 1 2019/11/23
