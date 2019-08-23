---
tags: [2019/08/23, application/array/2-D, leetcode/566]
title: Reshape the Matrix
created: '2019-08-23T13:39:33.752Z'
modified: '2019-08-23T13:50:55.447Z'
---

# Reshape the Matrix

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

### Example 1:

```
Input:
nums = [[1,2], [3,4]]
r = 1, c = 4
Output: [[1,2,3,4]]

Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
```

### Example 2:

```
Input: nums = [[1,2], [3,4]]
r = 2, c = 4
Output: [[1,2], [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
```

> The height and width of the given matrix is in range [1, 100].
> The given r and c are all positive.

## Solution

```python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums

        matrix = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                s = i * c + j
                x = s / n
                y = s % n
                v = nums[x][y]
                matrix[i][j] = v
        return matrix
```
