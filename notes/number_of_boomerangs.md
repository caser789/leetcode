---
tags: [2019/09/23, leetcode/447]
title: Number of Boomerangs
created: '2019-09-07T08:39:16.819Z'
modified: '2019-09-19T05:31:52.791Z'
---

# Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

### Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

## Solution

```python
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                a = p[0] - q[0]
                b = p[1] - q[1]
                v = a*a + b*b
                cmap.setdefault(v, 0)
                cmap[v] += 1
            for k in cmap:
                res += cmap[k] * (cmap[k] - 1)
        return res
```


## schedule

* [x] 0 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [ ] 1 2019/09/23

