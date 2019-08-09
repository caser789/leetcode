---
tags: [2019/08/09, application/array/2-D, leetcode/733, method/traversal/bfs]
title: Flood Fill
created: '2019-08-09T15:07:21.143Z'
modified: '2019-08-09T15:20:43.804Z'
---

# Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

### Example 1:

```
Input:
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
sr = 1, sc = 1, newColor = 2
Output: [
    [2,2,2],
    [2,2,0],
    [2,0,1]
]

From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
```

> The length of image and image[0] will be in the range [1, 50].
> The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
> The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

## Solution

```python
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        seen = set()
        q = [(sr, sc)]
        seen.add((sr, sc))
        v = image[sr][sc]
        m = len(image)
        n = len(image[0])
        while q:
            next_q = []
            for x, y in q:
                image[x][y] = newColor
                for i, j in self.neighbours(image, x, y, m, n):
                    if (i, j) in seen: continue
                    if image[i][j] != v: continue
                    next_q.append((i, j))
                    seen.add((i, j))
            q = next_q
        return image

    def neighbours(self, image, x, y, m, n):
        if x - 1 >= 0:
            yield x - 1, y
        if x + 1 < m:
            yield x + 1, y
        if y - 1 >= 0:
            yield x, y - 1
        if y + 1 < n:
            yield x, y + 1

image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
Solution().floodFill(image, 1, 1, 2)
print image
```
