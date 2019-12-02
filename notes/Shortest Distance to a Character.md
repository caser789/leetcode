---
tags: [2019/11/06, leetcode/821]
title: Shortest Distance to a Character
created: '2019-10-08T14:50:06.067Z'
modified: '2019-10-22T14:59:03.504Z'
---

# Shortest Distance to a Character

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

## Solution

```python
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        stack = []
        n = len(S)
        left = [10000] * n
        
        for i, c in enumerate(S):
            if c != C:
                stack.append(i)
            else:
                left[i] = 0
                d = 1
                while stack:
                    j = stack.pop()
                    left[j] = d
                    d += 1
        
        stack = []
        right = [10000] * n
        for i in range(n-1, -1, -1):
            if S[i] != C:
                stack.append(i)
            else:
                right[i] = 0
                d = 1
                while stack:
                    j = stack.pop()
                    right[j] = d
                    d += 1
        
        return [min(left[i], right[i]) for i in range(n)]
                
                
                    
```

## schedule

* [x] 0 2019/10/11
* [x] 1 2019/10/12
* [x] 1 2019/10/15
* [x] 1 2019/10/22
* [ ] 1 2019/11/06

