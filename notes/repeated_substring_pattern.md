---
tags: [2019/10/31, knack, leetcode/459]
title: Repeated Substring Pattern
created: '2019-08-31T09:22:50.801Z'
modified: '2019-10-01T05:24:06.864Z'
---

# Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

### Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

### Example 2:

Input: "aba"
Output: False

### Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

## Solution

```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]
```

## schedule

* [x] 0 2019/09/04
* [x] 1 2019/09/05
* [x] 1 2019/09/08
* [x] 1 2019/09/15
* [x] 1 2019/09/30
* [ ] 1 2019/10/31
