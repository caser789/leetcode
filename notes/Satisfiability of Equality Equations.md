---
tags: [2019/10/30, leetcode/990]
title: Satisfiability of Equality Equations
created: '2019-10-30T15:20:23.436Z'
modified: '2019-10-30T15:22:15.030Z'
---

# Satisfiability of Equality Equations

Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

### Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

### Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

### Example 3:

Input: ["a==b","b==c","a==c"]
Output: true

### Example 4:

Input: ["a==b","b!=c","c==a"]
Output: false

### Example 5:

Input: ["c==c","b==d","x!=z"]
Output: true
 

## Note:

```
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] and equations[i][3] are lowercase letters
equations[i][1] is either '=' or '!'
equations[i][2] is '='
```


## Solution

```python
class UF(object):
    def __init__(self, n):
        self.n = n
        self.parents = range(n)
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        self.parents[root_q] = root_p
        self.n -= 1
    
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        uf = UF(26)

        
        for equation in equations:
            if equation[1] == '!':
                continue
            x = equation[0]
            y = equation[3]
            uf.union(ord(x)-ord('a'), ord(y)-ord('a'))
        
        for equation in equations:
            if equation[1] == '=':
                continue
            x = equation[0]
            y = equation[3]

            
            if uf.is_connected(ord(x)-ord('a'), ord(y)-ord('a')):
                return False
        return True
        
            
            
```

## schedule

* [x] 2019/10/29
* [ ] 2019/10/30
