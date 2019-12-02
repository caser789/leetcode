---
tags: [2019/11/07, leetcode/1037]
title: Valid Boomerang
created: '2019-10-08T15:00:45.009Z'
modified: '2019-10-23T11:14:03.311Z'
---

# Valid Boomerang

A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false
 

## Note:

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
 

## Solution

```python
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        a, b, c = points
        
        return (c[0] - b[0])*(b[1] - a[1]) != (b[0] - a[0])*(c[1] - b[1])
              

```

## schedule

* [x] 0 2019/10/12
* [x] 1 2019/10/13
* [x] 1 2019/10/16
* [x] 1 2019/10/23
* [ ] 1 2019/11/07
