---
tags: [2019/09/24]
title: Largest Triangle Area
created: '2019-09-22T11:14:58.323Z'
modified: '2019-09-22T11:15:34.152Z'
---

# Largest Triangle Area

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.

![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png)

Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.

## Solution

```
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        
```
