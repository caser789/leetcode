---
tags: [2019/11/24, application/permutation, leetcode/996, method/backtrack]
title: Number of Squareful Arrays
created: '2019-11-24T11:50:57.778Z'
modified: '2019-11-24T11:51:47.597Z'
---

# Number of Squareful Arrays

Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

 

Example 1:

Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: [2,2,2]
Output: 1
 

Note:

1 <= A.length <= 12
0 <= A[i] <= 1e9


## Solution

```python
import math
class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        n = len(A)
        seen = [False] * n
        tmp = []
        self.count = 0
        def is_valid(m):
            i = int(math.sqrt(m))
            return i*i == m
            
        def search(cnt):
            if cnt > 1:
                if not is_valid(tmp[-1] + tmp[-2]): return
            if cnt == n:
                self.count += 1
                
                return
            
            for i in range(n):
                if seen[i]: continue
                if i > 0 and A[i] == A[i-1] and not seen[i-1]: continue
                    
                tmp.append(A[i])
                seen[i] = True
                
                search(cnt+1)
                
                seen[i] = False
                tmp.pop()
        
        search(0)
        return self.count
```

## refs

* [lc](https://leetcode.com/problems/number-of-squareful-arrays/)

