---
tags: [2019/08/13, leetcode/118, method/recursion]
title: Pascal's Triangle
created: '2019-08-13T15:17:05.885Z'
modified: '2019-08-13T15:21:47.044Z'
---

#  Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

![pic](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

In Pascal's triangle, each number is the sum of the two numbers directly above it.

### Example:

```
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

## Solution

```python
class Solution(object):
    def _generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(2, numRows+1):
            row = [1]
            for j in range(1, i-1):
                row.append(res[i-2][j] + res[i-2][j-1])
            row.append(1)
            res.append(row)
        return res

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        res = self.generate(numRows-1)
        last = res[-1]
        row = [1]
        for i in range(1, len(last)):
            row.append(last[i]+last[i-1])
        row.append(1)
        res.append(row)
        return res

```
