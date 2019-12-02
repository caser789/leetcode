---
tags: [2019/11/15, application/combination, leetcode/1239, method/backtrack]
title: Maximum Length of a Concatenated String with Unique Characters
created: '2019-11-15T14:21:21.368Z'
modified: '2019-11-23T14:50:11.890Z'
---

# Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.


## Solution

```python
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        arr = [e for e in arr if len(e) == len(set(e))]
        res = []
        
        def collect(i, seen, tmp):
            
            res.append(''.join(tmp))
            
            for j in range(i, len(arr)):
                s = arr[j]
                valid = True
                for c in s:
                    if seen.get(c, 0) > 0:
                        valid = False
                        break
                
                if not valid: continue
                
                for c in s:
                    seen.setdefault(c, 0)
                    seen[c] += 1
                    
                tmp.append(s)
                collect(j+1, seen, tmp)
                tmp.pop()
                    
                for c in s:
                    seen[c] -= 1
            
        
        seen = {}
        
        collect(0, seen, [])
        
        return max(len(e) for e in res)
```

## refs

* [lc](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)
