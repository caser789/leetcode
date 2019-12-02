---
tags: [2019/11/07, leetcode/796, method/kmp, method/rolling_hash]
title: Rotate String
created: '2019-09-24T15:28:26.261Z'
modified: '2019-10-27T04:38:46.460Z'
---

# Rotate String

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.

## Solution

```python
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and A in B+B
        
```

## schedule

* [x] 0 2019/10/01
* [x] 1 2019/10/02
* [x] 1 2019/10/05
* [x] 1 2019/10/12
* [x] 1 2019/10/27
* [ ] 1 2019/11/27
