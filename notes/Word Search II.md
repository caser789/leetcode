---
tags: [2019/11/25, application/best_path, data structure/trie, method/backtrack, TODO]
title: Word Search II
created: '2019-11-25T02:41:24.957Z'
modified: '2019-11-25T02:53:06.398Z'
---

# Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

## Solution

### brute force

```python
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(board)
        m = len(board[0])
        
        def find(word):
            length = len(word)
            
            def search(i, x, y):
                if i == length-1:
                    return True

                board[x][y] = '#'
                for xx, yy in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == word[i+1]:
                        if search(i+1, xx, yy):
                            board[x][y] = word[i]
                            return True
                board[x][y] = word[i]
                        
                return False
                  
            for i in range(n):
                for j in range(m):
                    if word[0] == board[i][j]:
                        if search(0, i, j):
                            return True
            return False
            
        res = []
        for word in words:
            if find(word):
                res.append(word)
        return res
```

## refs

* [lc](https://leetcode.com/problems/word-search-ii/)

