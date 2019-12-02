---
tags: [2019/11/25, leetcode/37]
title: Sudoku Solver
created: '2019-11-25T12:07:05.018Z'
modified: '2019-11-25T12:30:11.994Z'
---

# Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
Accepted

![pic](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
![pic](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)

## Solution

```python
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if not n:
            return
        m = len(board[0])
        if not m:
            return
        
        def is_valid(row, col, c):
            for i in range(9):
                if board[row][i] == c: return False
                if board[i][col] == c: return False
                if board[row/3*3+i/3][col/3*3+i%3] == c: return False
            return True
        
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.': continue   
                    for c in '123456789':
                        if is_valid(i, j, c):
                            board[i][j] = c
                            if solve():
                                return True
                            board[i][j] = '.'
                    return False   
            return True
        
        
        solve()

```

## refs

* [lc](https://leetcode.com/problems/sudoku-solver/submissions/)

