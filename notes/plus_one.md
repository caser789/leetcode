---
tags: [2019/08/29, application/add, leetcode/66]
title: Plus One
created: '2019-08-29T15:37:54.610Z'
modified: '2019-08-29T15:41:42.550Z'
---

# Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

### Example 1:

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

### Example 2:

```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

## Solution

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        carry = 1
        for d in digits[::-1]:
            carry, v = divmod(d+carry, 10)
            res.append(v)
        if carry:
            res.append(carry)
        return res[::-1]
```
