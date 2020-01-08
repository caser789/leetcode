---
tags: [2020/01/07, leetcode/76, method/sliding-window]
title: Minimum Window Substring
created: '2020-01-06T14:02:04.006Z'
modified: '2020-01-06T14:18:31.267Z'
---

# Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

## Solution

```python
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        counter = Counter(t)
        required = len(counter)
        
        i = j = 0
        
        formed = 0
        
        cur_counter = {}
        
        res = (float('inf'), None, None)
        
        while j < len(s):
            c = s[j]
            cur_counter[c] = cur_counter.get(c, 0) + 1
            
            if c in counter and cur_counter[c] == counter[c]:
                formed += 1
            
            while i <= j and formed == required:
                c = s[i]
                
                if j - i + 1 < res[0]:
                    res = (j-i+1, i, j)
                
                cur_counter[c] -= 1
                
                if c in counter and cur_counter[c] < counter[c]:
                    formed -= 1
                
                i += 1
            j += 1
        
        return '' if res[0] == float('inf') else s[res[1]:res[2]+1]
            
```

### better sliding-window

```python
from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''
        
        fp = Counter(t)
        char_cnt = len(fp)
        
        lst = [(i, c) for i, c in enumerate(s) if c in fp]
        
        i = j = 0
        cur_char_cnt = 0
        cur_fp = {}
        res = (float('inf'), None, None)
        
        while j < len(lst):
            c = lst[j][1]
            cur_fp[c] = cur_fp.get(c, 0) + 1
            
            if cur_fp[c] == fp[c]:
                cur_char_cnt += 1
            
            while i <= j and cur_char_cnt == char_cnt:
                y = lst[j][0]
                x = lst[i][0]
                if y - x + 1 < res[0]:
                    res = (y-x+1, x, y)
                
                c = lst[i][1]
                cur_fp[c] -= 1
                if cur_fp[c] < fp[c]:
                    cur_char_cnt -= 1
                i += 1
                
            j += 1
        return '' if res[0] == float('inf') else s[res[1]:res[2]+1]
            
```

## schedule

* [x] 2020/01/06
* [ ] 2020/01/07

## refs

* [lc](https://leetcode.com/problems/minimum-window-substring/)
