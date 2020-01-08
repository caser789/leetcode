---
tags: [2019/12/31, leetcode/130, method/union find]
title: Surrounded Regions
created: '2019-12-02T05:17:07.013Z'
modified: '2019-12-30T14:48:44.572Z'
---

# Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

## Solution

```python
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if not n: return
        m = len(board[0])
        if not m: return
        
        k = n * m + 1
        uf = UF(k)
        
        for i in range(n):
            for j in range(m):
                a = j * n + i
                if i in (0, n-1) or j in (0, m-1):
                    uf.union(a, k-1)
                else:
                    for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                        if not 0 <= x < n: continue
                        if not 0 <= y < m: continue
                        if board[x][y] == board[i][j]:
                            b = y * n + x
                            uf.union(a, b)
        
        for i in range(n):
            for j in range(m):
                a = j * n + i
                if board[i][j] == 'O' and not uf.connected(a, k-1):
                    board[i][j] = 'X'
                
        
class UF(object):
    
    def __init__(self, n):
        self.n = n
        self.parents = range(n)
        self.size = [1] * n
    
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def union(self, p, q):
        pp = self.find(p)
        qq = self.find(q)
        if pp == qq:
            return
        
        if self.size[qq] < self.size[pp]:
            self.size[pp] += self.size[qq]
            self.parents[qq] = pp
        else:
            self.parents[pp] = qq
            self.size[qq] += self.size[pp]
        self.n -= 1
        
    def connected(self, p, q):
        return self.find(p) == self.find(q)       
```

## schedule

* [x] 2019/12/30
* [ ] 2019/12/31

## refs

* [lc](https://leetcode.com/problems/surrounded-regions/)
