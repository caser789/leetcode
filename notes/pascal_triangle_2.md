---
tags: [2019/08/13, leetcode/119, method/recursion]
title: Pascal's Triangle II
created: '2019-08-13T15:21:50.707Z'
modified: '2019-08-13T15:22:40.142Z'
---

# Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

### Example:

```
Input: 3
Output: [1,3,3,1]
```

> Could you optimize your algorithm to use only O(k) extra space?

## Solution

```python
class Solution(object):
    def _getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        last = [1]
        if rowIndex == 0:
            return last
        for i in range(1, rowIndex+1):
            row = [1]
            for j in range(1, len(last)):
                row.append(last[j] + last[j-1])
            row.append(1)
            last = row
        return last

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        last = [1]
        if rowIndex == 0:
            return last
        last = self.getRow(rowIndex-1)
        row = [1]
        for i in range(1, len(last)):
            row.append(last[i]+last[i-1])
        row.append(1)
        return row
```
