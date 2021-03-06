---
tags: [2019/08/18, leetcode/34, method/search/binary]
title: Find First and Last Position of Element in Sorted Array
created: '2019-08-18T09:31:18.313Z'
modified: '2019-08-18T09:31:55.227Z'
---

# Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

### Example 1:

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Example 2:

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

## Solution

```python
class Solution(object):

    def find_right(self, nums, target):
        """
        >>> nums = [5, 7, 7, 8, 8, 10]
        >>> target = 8
        >>> Solution().find_right(nums, target)
        4
        >>> nums = [5, 7, 7, 8, 8, 10]
        >>> target = 11
        >>> Solution().find_right(nums, target)
        -1
        >>> nums = [5, 7, 7, 8, 8, 10]
        >>> target = 3
        >>> Solution().find_right(nums, target)
        -1
        """
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mi = (lo+hi+1)/2
            v = nums[mi]
            if v == target:
                lo = mi
            elif v < target:
                lo = mi + 1
            else:
                hi = mi - 1

        if not 0 <= lo < len(nums):
            return -1
        return lo if nums[lo] == target else -1

    def find_left(self, nums, target):
        """
        >>> nums = [5, 7, 7, 8, 8, 10]
        >>> target = 8
        >>> Solution().find_left(nums, target)
        3
        """
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mi = (lo+hi)/2
            v = nums[mi]
            if v == target:
                hi = mi
            elif v < target:
                lo = mi + 1
            else:
                hi = mi - 1
        if not 0 <= lo < len(nums):
            return -1
        return lo if nums[lo] == target else -1

    def searchRange(self, nums, target):
        """
        >>> nums = [5, 7, 7, 8, 8, 10]
        >>> target = 8
        >>> Solution().searchRange(nums, target)
        [3, 4]
        >>> nums = [5, 7, 7, 8, 8, 10]
        >>> target = 6
        >>> Solution().searchRange(nums, target)
        [-1, -1]
        """
        return [self.find_left(nums, target), self.find_right(nums, target)]
```
