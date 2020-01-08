---
tags: [2019/12/22, data structure/priority queue, leetcode/407]
title: Trapping Rain Water II
created: '2019-12-15T11:29:24.475Z'
modified: '2019-12-21T10:42:35.763Z'
---

# Trapping Rain Water II

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

 

Note:

Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

 

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

![pic](https://assets.leetcode.com/uploads/2018/10/13/rainwater_empty.png)
![pic](https://assets.leetcode.com/uploads/2018/10/13/rainwater_fill.png)
 



After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

## Solution

```python
class Solution(object):
    def trapRainWater(self, grid):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        pq = []
        seen = set()
        
        for i in (0, n-1):
            for j in range(m):
                heapq.heappush(pq, (grid[i][j], i, j))
                seen.add((i, j))
        
        for j in (0, m-1):
            for i in range(n):
                if (i, j) in seen: continue
                heapq.heappush(pq, (grid[i][j], i, j))
                seen.add((i, j))

        res = 0
        mx = float('-inf')
        
        while pq:
            v, x, y = heapq.heappop(pq)
            mx = max(v, mx)
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if not 0 <= i < n: continue
                if not 0 <= j < m: continue
                if (i, j) in seen: continue
    
                if mx > grid[i][j]:
                    res += mx - grid[i][j]
                
                heapq.heappush(pq, (grid[i][j], i, j))
                seen.add((i, j))

        return res
```

## refs

* [lc](https://leetcode.com/problems/trapping-rain-water-ii/)
* [youtube](https://www.youtube.com/watch?v=cJayBq38VYw)


## schedule

* [x] 2019/12/21
* [ ] 2019/12/22

