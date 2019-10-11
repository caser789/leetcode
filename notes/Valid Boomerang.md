---
tags: [2019/10/09, leetcode/1037]
title: Valid Boomerang
created: '2019-10-08T15:00:45.009Z'
modified: '2019-10-08T15:01:19.246Z'
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
        
```
