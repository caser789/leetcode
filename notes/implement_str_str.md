---
favorited: true
tags: [2019/11/01, leetcode/28]
title: Implement strStr()
created: '2019-08-31T09:32:10.214Z'
modified: '2019-10-03T05:25:12.108Z'
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

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        if m > n:
            return -1
        if m == n:
            if haystack != needle:
                return -1
            return 0
        for i in range(n-m+1):
            j = 0
            while j < m and haystack[i+j] == needle[j]:
                j += 1
            if j == m:
                return i
        return -1
```

## schedule

* [x] 0 2019/09/05
* [x] 1 2019/09/06
* [x] 1 2019/09/07
* [x] 1 2019/09/10
* [x] 1 2019/09/17
* [x] 1 2019/10/01
* [ ] 1 2019/11/01
