---
tags: [2019/11/16, application/n-queen, leetcode/52, method/backtrack]
title: N-Queens II
created: '2019-11-16T11:27:59.201Z'
modified: '2019-11-25T04:24:29.009Z'
---

# N-Queens II

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![pic](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)


Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

## Solution

```python
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cnt = 0
        def valid(i, j, lst):
            for x, y in lst:
                if i == x: return False
                if j == y: return False
                if x - i == y - j: return False
                if x - i == j - y: return False
            return True
        
        def collect(r, tmp):
            if r == n:
                self.cnt += 1
                return
            
            for c in range(n):
                if valid(r, c, tmp):
                    tmp.append((r, c))
                    collect(r+1, tmp)
                    tmp.pop()
                    
        
        collect(0, [])
        return self.cnt
            
```

## refs

* [lc](https://leetcode.com/problems/n-queens-ii/)
