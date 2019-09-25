---
tags: [2019/09/27, leetcode/461]
title: Hamming Distance
created: '2019-09-22T11:07:14.511Z'
modified: '2019-09-24T05:04:59.720Z'
---

# Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

## Note:
0 ≤ x, y < 231.

### Example:

Input: x = 1, y = 4

Output: 2

Explanation:

```
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
```

The above arrows point to positions where the corresponding bits are different.

## Solution

```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        Input: x = 1, y = 4
        Output: 2
        0001
        0100
        """
        A = []
        while x > 0:
            x, c = divmod(x, 2)
            A.append(c)
        B = []
        while y > 0:
            y, c = divmod(y, 2)
            B.append(c)
        n = len(A)
        m = len(B)
        res = 0
        i = 0
        j = 0
        while i < n and j < m:
            if A[i] != B[j]:
                res += 1
            i += 1
            j += 1

        while i < n:
            if A[i] == 1:
                res += 1
            i += 1
        while j < m:
            if B[m] == 1:
                res += 1
            j += 1
        return res
```

## schedule

* [x] 0 2019/09/23
* [x] 1 2019/09/24
* [ ] 1 2019/09/27
