---
tags: [2019/08/18, leetcode/392, method/search/binary]
title: Is Subsequence
created: '2019-08-18T10:14:01.534Z'
modified: '2019-08-18T10:33:20.131Z'
---

# Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
> If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?


## Solution

```python
from bisect import bisect_left


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        store = {}
        for i, c in enumerate(t):
            store.setdefault(c, [])
            store[c].append(i)

        # lo is the mim index the current char has to be at
        lo = 0
        for c in s:
            if c not in store:
                return False
            index_list = store[c]
            # try to find an index that is larger than or equal to lo
            i = bisect_left(index_list, lo)
            if i == len(index_list):
                return False
            lo = index_list[i] + 1
        return True
```
