---
tags: [2019/09/01, knack, leetcode/521]
title: Longest Uncommon Subsequence I
created: '2019-08-31T08:52:26.313Z'
modified: '2019-09-01T04:50:08.849Z'
---

# Longest Uncommon Subsequence I


Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

### Example 1:

Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"),
because "aba" is a subsequence of "aba",
but not a subsequence of any other strings in the group of two strings.

## Note:

* Both strings' lengths will not exceed 100.
* Only letters from a ~ z will appear in input strings.


## Solution


### intuitive

```python
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        s_to_cnt = {}
        for s in [a, b]:
            n = len(s)
            for i in range(n):
                for j in range(n+1):
                    sub_s = s[i:j]
                    if not sub_s: continue
                    s_to_cnt.setdefault(sub_s, 0)
                    s_to_cnt[sub_s] += 1

        max_len = 0
        for k, v in s_to_cnt.items():
            if v != 1: continue
            max_len = max(max_len, len(k))
        return max_len
```

### knack

```python
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))
```
