---
tags: [binary search/2]
title: Find Peak Element
created: '2019-08-02T05:49:51.667Z'
modified: '2019-08-02T05:50:16.338Z'
---

# Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

### Example 1:

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

### Example 2:

```
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

> Your solution should be in logarithmic complexity.

## Solution

```python
class Solution(object):
    def findPeakElement(self, nums):
        """
        >>> Solution().findPeakElement([1, 2, 3, 1])
        2
        >>> Solution().findPeakElement([4, 2, 3, 1])
        0
        >>> Solution().findPeakElement([1, 2, 3, 4])
        3
        >>> Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
        1
        """
        n = len(nums)

        if not n:
            return

        lo = 0
        hi = n-1
        while lo < hi:
            mi1 = (lo+hi) / 2
            mi2 = mi1+1
            if nums[mi1] < nums[mi2]:
                lo = mi2
            else:
                hi = mi1
        return lo
```
