---
tags: [2019/12/29, application/best_path, data structure/trie, leetcode/212, method/backtrack]
title: Word Search II
created: '2019-11-25T02:41:24.957Z'
modified: '2019-12-29T08:42:12.352Z'
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

### trie

```python
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        t = Trie()
        for word in words:
            t[word] = True

        return t.search(board)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.index = -1


class Trie(object):

    def __init__(self):
        self.root = None

    def __setitem__(self, k, v):
        self.root = self._set_node(self.root, k, v, 0)

    def _set_node(self, node, k, v, i):
        if node is None:
            node = Node(None)
            node.index = i - 1

        if i == len(k):
            node.val = v
            return node

        c = k[i]
        j = ord(c) - ord('a')
        node.children[j] = self._set_node(node.children[j], k, v, i+1)
        return node

    def search(self, board):
        res = set()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                seen = set()
                self._search(self.root, board, i, j, n, m, seen, res, [], -1)
        return list(res)

    def _search(self, node, board, i, j, n, m, seen, res, prefix, index):
        if node is None:
            return

        if node.index != index:
            return

        if node.val:
            res.add(''.join(prefix))

        if not 0 <= i < n:
            return

        if not 0 <= j < m:
            return

        if (i, j) in seen:
            return
        seen.add((i, j))

        c = board[i][j]
        k = ord(c) - ord('a')
        node = node.children[k]
        prefix.append(c)

        for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            self._search(node, board, x, y, n, m, seen, res, prefix, index+1)

        prefix.pop()
        seen.remove((i, j))


```

### default dict

```python
from collections import defaultdict

T = lambda: defaultdict(T)
END = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        t = T()
        
        for word in words:
            reduce(dict.__getitem__, word, t)[END] = word
            
        n = len(board)
        m = len(board[0]) 
        
        def bfs(d, i, j, seen, res):
            if not 0 <= i < n: 
                return
            
            if not 0 <= j < m:
                return
            
            if not isinstance(d, dict):
                return
            
            c = board[i][j]
            if c not in d:
                return
            
            if (i, j) in seen:
                return
            seen.add((i, j))
            
            d = d[c]
            if END in d:
                res.add(d[END])

            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)): 
                bfs(d, x, y, seen, res)

            seen.remove((i, j))
                
        
        res = set()

        for i in range(n):
            for j in range(m):
                bfs(t, i, j, set(), res)
        return list(res)

```

## refs

* [lc](https://leetcode.com/problems/word-search-ii/)

## schedule

* [x] 2019/12/28
* [x] 2019/12/29
* [ ] 2020/01/01
