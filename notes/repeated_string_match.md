---
tags: [2019/09/06, leetcode/686, TODO]
title: Repeated String Match
created: '2019-08-31T09:36:24.127Z'
modified: '2019-08-31T09:36:44.724Z'
---

# Repeated String Match

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

## Note:

The length of A and B will be between 1 and 10000.

## Solution

```python
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

```
