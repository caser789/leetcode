---
favorited: true
tags: [2019/11/01, data structure/trie, leetcode/14]
title: Longest Common Prefix
created: '2019-08-31T09:30:15.689Z'
modified: '2019-10-03T05:20:25.362Z'
---

# Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

### Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

## Note:

All given inputs are in lowercase letters a-z.

## Solution

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        n = len(strs)
        if not n:
            return ''
        m = min(len(strs[i]) for i in range(n))

        i = 0
        res = []
        done = False
        while i < m and not done:
            v = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != v:
                    done = True
            if not done:
                res.append(v)
            i += 1
        return ''.join(res)

```

## schedule

* [x] 0 2019/09/05
* [x] 1 2019/09/06
* [x] 1 2019/09/09
* [x] 1 2019/09/16
* [x] 1 2019/10/01
* [ ] 1 2019/11/01
