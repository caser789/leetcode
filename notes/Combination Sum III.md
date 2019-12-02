---
tags: [2019/11/15, application/combination, leetcode/216, method/backtrack]
title: Combination Sum III
created: '2019-11-15T04:57:22.949Z'
modified: '2019-11-23T10:29:03.667Z'
---

# Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]


## Solution

```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        1-9
        """
        res = []

        def collect(i, tmp):
            if sum(tmp) > n:
                return
            if len(tmp) > k:
                return

            if len(tmp) == k:
                if sum(tmp) == n:
                    res.append(tmp[:])
                return

            for j in range(i+1, 10):
                tmp.append(j)

                collect(j, tmp)

                tmp.pop()

        tmp = []
        collect(0, tmp)
        return res
      
```

### better

```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        res = []
                
        def find(tmp, nn, i, kk):
            if nn < 0:
                return
            if kk == 0:
                if nn == 0:
                    res.append(tmp[:])
                return
                         
            for j in range(i, 10):
                tmp.append(j)
                find(tmp, nn-j, j+1, kk-1)
                tmp.pop()
        
        
        find([], n, 1, k)
        
        return res
```

## refs

* [lc](https://leetcode.com/problems/combination-sum-iii/submissions/)


