---
tags: [2019/08/22, application/array/2-D, leetcode/840]
title: Magic Squares In Grid
created: '2019-08-22T12:50:15.981Z'
modified: '2019-08-22T13:45:13.511Z'
---

# Magic Squares In Grid

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

### Example 1:

```
Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
```

> 1 <= grid.length <= 10
> 1 <= grid[0].length <= 10
> 0 <= grid[i][j] <= 15


## Solution

```python
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def is_magic(a, b, c, d, e, f, g, h, i):
            return (
                sorted([a, b, c, d, e, f, g, h, i]) == range(1, 10) and
                (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15)
            )

        ans = 0
        for i in range(m-2):
            for j in range(n-2):
                if grid[i+1][j+1] != 5: continue
                if is_magic(grid[i][j], grid[i][j+1], grid[i][j+2],
                         grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                         grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]):
                    ans += 1
        return ans
```
