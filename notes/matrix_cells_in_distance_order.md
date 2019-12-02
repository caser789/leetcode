---
tags: [2019/11/11, leetcode/1030]
title: Matrix Cells in Distance Order
created: '2019-09-07T09:24:35.935Z'
modified: '2019-10-12T07:19:36.244Z'
---

# Matrix Cells in Distance Order

We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)



### Example 1:

Input: R = 1, C = 2, r0 = 0, c0 = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (r0, c0) to other cells are: [0,1]

### Example 2:

Input: R = 2, C = 2, r0 = 0, c0 = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

### Example 3:

Input: R = 2, C = 3, r0 = 1, c0 = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].


## Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C

## Solution

```python
from collections import deque
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        seen = [[0 for _ in range(C)] for _ in range(R)]

        q = deque()

        res = []
        q.append([r0, c0])

        while q:
            x, y = q.popleft()
            if not 0 <= x < R:
                continue
            if not 0 <= y < C:
                continue

            if seen[x][y]:
                continue
            res.append([x, y])
            seen[x][y] = 1
            q.append([x+1, y])
            q.append([x-1, y])
            q.append([x, y+1])
            q.append([x, y-1])
        return res
```

## schedule

* [x] 0 2019/09/15
* [x] 1 2019/09/16
* [x] 1 2019/09/19
* [x] 1 2019/09/26
* [x] 1 2019/10/11
* [ ] 1 2019/11/11
