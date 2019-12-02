---
tags: [2019/11/04, application/best_path, leetcode/79, method/backtrack]
title: Word Search
created: '2019-11-03T02:49:35.648Z'
modified: '2019-11-25T03:56:12.896Z'
---

# Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example:

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


## Solution

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if _exist(board, i, j, word, 0):
                    return True
        return False

def _exist(board, i, j, word, k):
    if k == len(word): return True
    if i < 0: return False
    if j < 0: return False
    if i == len(board): return False
    if j == len(board[0]): return False
    if board[i][j] != word[k]: return False
    s = board[i][j]
    board[i][j] = '#'
    res = (
        _exist(board, i+1, j, word, k+1) or
        _exist(board, i-1, j, word, k+1) or
        _exist(board, i, j+1, word, k+1) or
        _exist(board, i, j-1, word, k+1)
    )
    board[i][j] = s
    return res
```

### better backtrack

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])
        k = len(word)
        
        def search(i, x, y):
            if i == k - 1:
                return True
            board[x][y] = '#'
            for xx, yy in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == word[i+1]:
                    if search(i+1, xx, yy):
                        return True
            board[x][y] = word[i]
            return False
            
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if search(0, i, j): return True
        return False
                
```

## Schedule

* [x] 2019/11/03
* [ ] 2019/11/04

## refs

* [lc](https://leetcode.com/problems/word-search/)
