---
tags: [2019/09/06, leetcode/28, TODO]
title: Implement strStr()
created: '2019-08-31T09:32:10.214Z'
modified: '2019-09-05T14:17:45.323Z'
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

        if not n and not m:
            return 0

        for i in range(n):

            if n - i < m:
                return -1

            done = False
            j = 0
            while j < m and not done:
                if haystack[i+j] != needle[j]:
                    done = True
                else:
                    j += 1
            if not done:
                return i
        return -1

```

## schedule

* [x] 0 2019/09/05
* [ ] 1 2019/09/06
