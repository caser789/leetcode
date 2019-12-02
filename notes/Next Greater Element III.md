---
tags: [2019/11/21]
title: Next Greater Element III
created: '2019-11-21T14:21:14.977Z'
modified: '2019-11-21T14:21:58.539Z'
---

# Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1

## Solution

```python
class Solution(object):
    def nextGreaterElement(self, m):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(m))
        n = len(digits)
        i = n - 2
        while i >= 0 and digits[i] >= digits[i+1]:
            i -= 1

        if i < 0:
            return -1

        j = n - 1
        while digits[j] <= digits[i]:
            j -= 1

        swap(digits, i, j)
        reverse(digits, i+1, n-1)
        
        res = int(''.join(digits))
        return res if res <= 1<<31-1 else -1


def swap(digits, i, j):
    digits[i], digits[j] = digits[j], digits[i]


def reverse(digits, i, j):
    while i < j:
        digits[i], digits[j] = digits[j], digits[i]
        i += 1
        j -= 1

```

## refs

* [lc](https://leetcode.com/problems/next-greater-element-iii/)
* [dis](https://leetcode.com/problems/next-greater-element-iii/discuss/101824/Simple-Java-solution-(4ms)-with-explanation.)

