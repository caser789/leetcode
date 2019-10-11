---
tags: [2019/10/11, leetcode/976]
title: Largest Perimeter Triangle
created: '2019-09-07T09:26:09.635Z'
modified: '2019-09-26T05:07:52.954Z'
---

# Largest Perimeter Triangle

Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.



### Example 1:

Input: [2,1,2]
Output: 5

### Example 2:

Input: [1,2,1]
Output: 0

### Example 3:

Input: [3,2,3,4]
Output: 10

### Example 4:

Input: [3,6,2,3]
Output: 8


## Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6

## Solution

```python
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        n = len(A)
        if n < 3:
            return False
        a = A[-1]
        b = A[-2]
        for i in range(n-3, -1, -1):
            if A[i] + b > a:
                return A[i] + b + a
            else:
                a, b = b, A[i]
        return 0
```


## schedule

* [x] 0 2019/09/15
* [x] 1 2019/09/16
* [x] 1 2019/09/19
* [x] 1 2019/09/26
* [ ] 1 2019/10/11
