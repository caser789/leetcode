---
tags: [2019/08/27]
title: Toeplitz Matrix
created: '2019-08-28T13:43:14.439Z'
modified: '2019-08-28T13:43:25.883Z'
---

# Toeplitz Matrix

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


### Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

### Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

## Note:

> matrix will be a 2D array of integers.
> matrix will have a number of rows and columns in range [1, 20].
> matrix[i][j] will be integers in range [0, 99].

## Follow up:

> What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
> What if the matrix is so large that you can only load up a partial row into the memory at once?

## Solution

### Intuition

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for r in range(1, m):
            if not self.has_same_elements(r, 0, matrix, m, n):
                return False
        for c in range(n):
            if not self.has_same_elements(0, c, matrix, m, n):
                return False
        return True

    def has_same_elements(self, i, j, matrix, m, n):
        v = matrix[i][j]
        while i + 1 < m and j + 1 < n:
            i += 1
            j += 1
            if matrix[i][j] != v:
                return False
        return True
```

###  Hash

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        groups = {}
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                group = r - c
                if group not in groups:
                    groups[group] = v
                elif groups[group] != v:
                    return False
        return True
```

### Other

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                if r == 0: continue
                if c == 0: continue
                if v != matrix[r-1][c-1]: return False
        return True
```
