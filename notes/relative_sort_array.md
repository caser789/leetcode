---
tags: [2019/08/27, leetcode/1122, method/index]
title: Relative Sort Array
created: '2019-08-27T14:49:48.004Z'
modified: '2019-08-27T15:01:07.327Z'
---

# Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

### Example 1:

```
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
```

> arr1.length, arr2.length <= 1000
> 0 <= arr1[i], arr2[i] <= 1000
> Each arr2[i] is distinct.
> Each arr2[i] is in arr1.

## Solution

```python
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        frequencies = [0] * 1001
        for num in arr1:
            frequencies[num] += 1
        res = []
        for num in arr2:
            for _ in range(frequencies[num]):
                res.append(num)
            frequencies[num] = 0

        for i, cnt in enumerate(frequencies):
            if not cnt: continue
            for _ in range(cnt):
                res.append(i)
        return res
```
