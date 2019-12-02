---
tags: [2019/11/03, leetcode/567]
title: Permutation in String
created: '2019-11-02T15:07:37.625Z'
modified: '2019-11-02T15:08:36.677Z'
---

# Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


## Solution

```python
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        
        counter = {}
        for c in s1:
            counter.setdefault(c, 0)
            counter[c] += 1
        
        i = 0
        length = 0
        d = {}
        while i < m:
            c = s2[i]
            if c in counter:
                d.setdefault(c, 0)
                d[c] += 1
                length += 1
                if length == n:
                    if d == counter:
                        return True
                    length -= 1
                    cc = s2[i-n+1]
                    d[cc] -= 1
            else:
                d = {}
                length = 0
            i += 1
        return False
```

## schedule

* [x] 2019/11/02
* [ ] 2019/11/03

## refs

* [lc](https://leetcode.com/problems/permutation-in-string/)
