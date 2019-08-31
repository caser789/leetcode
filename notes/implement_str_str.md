---
tags: [2019/09/05, leetcode/28, TODO]
title: Implement strStr()
created: '2019-08-31T09:32:10.214Z'
modified: '2019-08-31T09:32:24.639Z'
---

# Implement strStr()


Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

### Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

### Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


## Solution

```
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

```
