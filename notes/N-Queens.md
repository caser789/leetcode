---
tags: [2019/11/16, application/n-queue, leetcode/51, method/backtrack]
title: N-Queens
created: '2019-11-16T13:24:06.582Z'
modified: '2019-11-25T04:10:54.945Z'
---

# N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![pic](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

## Solution

```python
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        
        
        def is_valid(i, j, tmp):
            for x, y in tmp:
                if i == x: return False
                if j == y: return False
                if i - x == j - y: return False
                if i - x == y - j: return False
            return True
        
        res = []
        def collect(r, tmp):
            if r == n: 
                matrix = [['.']*n for _ in range(n)]
                for x, y in tmp:
                    matrix[x][y] = 'Q'
                matrix = [''.join(row) for row in matrix]
                res.append(matrix)
                return
            for c in range(n):
                if is_valid(r, c, tmp):
                    tmp.append((r, c))
                    collect(r+1, tmp)
                    tmp.pop()
                    
        
        
        collect(0, [])
        return res
        
```

## refs

* [lc](https://leetcode.com/problems/n-queens/)

