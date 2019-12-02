---
tags: [2019/11/16, application/combination, leetcode/93, method/backtrack]
title: Restore IP Addresses
created: '2019-11-16T10:44:50.294Z'
modified: '2019-11-23T15:31:17.243Z'
---

# Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

## Solution

```
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(s)
        
        def collect(tmp, i):
            if len(tmp) == 4:
                if i == n:
                    res.append('.'.join(tmp))

                return
            
            word = []
            for j in range(3):
                if i + j < n:
                    word.append(s[i+j])
                    w = ''.join(word)
                    if not 0 <= int(w) < 256: continue
                    if len(w) > 1 and w.startswith('0'): continue
                    
                    
                    tmp.append(w)
                    collect(tmp, i+j+1)
                    tmp.pop()
                
        
        collect([], 0)
        return res
```

### better

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        res = []
        def find(i, tmp, length):
            if length == 0:
                if i == n:
                    res.append('.'.join(tmp))
                return
            if length < 0:
                return
            if i == n:
                return
            
            for j in range(3):
                if i + j == n:
                    break
                
                if j == 1 and s[i] == '0':
                    break
                
                if not 0 <= int(s[i:i+j+1]) < 256:
                    break
                
                tmp.append(s[i:i+j+1])
                find(i+j+1, tmp, length-1)
                tmp.pop()
        
        find(0, [], 4)
        return res
                    
                    
```

## refs

* [lc](https://leetcode.com/problems/restore-ip-addresses/)


