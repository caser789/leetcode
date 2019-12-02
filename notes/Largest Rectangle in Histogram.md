---
favorited: true
tags: [2019/10/28, data structure/monoqueue, leetcode/84]
title: Largest Rectangle in Histogram
created: '2019-10-27T13:07:34.925Z'
modified: '2019-11-21T01:17:14.696Z'
---

# Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 
![pic](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

![pic](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10

## Solution

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        n = len(heights)
        less_at_left = [0] * n
        less_at_right = [0] * n
        less_at_right[n-1] = n
        less_at_left[0] = -1

        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_at_left[p]
            less_at_left[i] = p

        for i in range(n-2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = less_at_right[p]
            less_at_right[i] = p

        res = 0
        for i in range(n):
            res = max(res, heights[i]*(less_at_right[i] - less_at_left[i] - 1))
        return res

```

## Schedule

* [x] 2019/10/27
* [ ] 2019/10/28
