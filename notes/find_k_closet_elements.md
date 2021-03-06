---
tags: [2019/08/18, application/array/k-closest, leetcode/658, method/search/binary/3]
title: Find K Closest Elements
created: '2019-08-02T05:56:10.295Z'
modified: '2019-08-18T10:12:12.408Z'
---

# Find K Closest Elements

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

### Example 1:

```
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
```

### Example 2:

```
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
```

> The value k is positive and will always be smaller than the length of the sorted array.
> Length of the given array is positive and will not exceed 104
> Absolute value of elements in the array and x will not exceed 104
> The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.


## Solution

```python
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        >>> Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3)
        [1, 2, 3, 4]
        """
        lo = 0
        hi = len(arr)-k
        while lo < hi:
            mi = (lo+hi) / 2
            if x - arr[mi] > arr[mi+k] - x:
                lo = mi + 1
            else:
                hi = mi
        return arr[lo:lo+k]
```
