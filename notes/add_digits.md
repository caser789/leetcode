---
tags: [2019/09/27, leetcode/258]
title: Add Digits
created: '2019-09-22T11:11:43.303Z'
modified: '2019-09-25T04:45:41.145Z'
---

# Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

## solution

```python
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num

        def _sum(n):
            s = 0
            while n:
                n, c = divmod(n, 10)
                s += c
            return s

        while num > 9:
            num = _sum(num)
        return num

```

## schedule

* [x] 0 2019/09/23
* [x] 1 2019/09/24
* [ ] 1 2019/09/27
