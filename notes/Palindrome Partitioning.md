---
tags: [2019/08/23, application/combination, leetcode/131, method/traceback]
title: Palindrome Partitioning
created: '2019-11-23T15:04:05.409Z'
modified: '2019-11-23T15:04:57.134Z'
---

# Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

## Solution

```
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        def is_par(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        res = []
        
        def find(i, tmp):
            if i == n:
                res.append(tmp[:])
                return
            
            for j in range(i, n):
                if not is_par(i, j):
                    continue
                
                tmp.append(s[i:j+1])
                find(j+1, tmp)
                tmp.pop()
                
        find(0, [])
        return res
```

## refs

* [lc](https://leetcode.com/problems/palindrome-partitioning/)

