---
tags: [2020/01/06, leetcode/959, method/union find]
title: Regions Cut By Slashes
created: '2019-12-02T05:20:37.924Z'
modified: '2020-01-05T07:41:59.780Z'
---

# Regions Cut By Slashes

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

 

### Example 1:

Input:
```
[
  " /",
  "/ "
]
```
Output: 2
Explanation: The 2x2 grid is as follows:

### Example 2:

Input:

```
[
  " /",
  "  "
]
```
Output: 1
Explanation: The 2x2 grid is as follows:

### Example 3:

```
Input:
[
  "\\/",
  "/\\"
]
```

Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

### Example 4:

```
Input:
[
  "/\\",
  "\\/"
]
```

Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

### Example 5:

```
Input:
[
  "//",
  "/ "
]
```
Output: 3
Explanation: The 2x2 grid is as follows:

 

## Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.


## Solution

```python
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        uf = UF(4*n*n)
        
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*n + c)
                if val in '/ ':
                    uf.union(root+0, root+1)
                    uf.union(root+2, root+3)
                if val in '\ ':
                    uf.union(root+0, root+3)
                    uf.union(root+1, root+2)
                
                if r + 1 < n:
                    uf.union(root+2, (root+4*n)+0)
                if r - 1 >= 0:
                    uf.union(root+0, (root-4*n)+2)
                if c + 1 < n:
                    uf.union(root+3, (root+4)+1)
                if c - 1 >= 0:
                    uf.union(root+1, (root-4)+3)
        

        return len(uf)
    
        
class UF(object):
    
    def __init__(self, n):
        self.n = n
        self.parents = range(n)
        self.ranks = [0] * n
    
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def union(self, p, q):
        u = self.find(p)
        v = self.find(q)
        if u == v:
            return
        
        if self.ranks[u] < self.ranks[v]:
            self.parents[u] = v
        elif self.ranks[u] > self.ranks[v]:
            self.parents[v] = u
        else:
            self.parents[u] = v
            self.ranks[v] += 1
        self.n  -= 1
        
    def __len__(self):
        return self.n
```

## schedule

* [x] 2020/01/05
* [ ] 2020/01/06

## refs

* [lc](https://leetcode.com/problems/regions-cut-by-slashes/)
