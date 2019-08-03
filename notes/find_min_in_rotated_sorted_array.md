---
tags: [binary search/2, minimum, peak, rotated]
title: Find Minimum in Rotated Sorted Array
created: '2019-08-02T05:50:42.988Z'
modified: '2019-08-03T08:20:05.195Z'
---

# Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

### Example 1:

```
Input: [3,4,5,1,2]
Output: 1
```

### Example 2:

```
Input: [4,5,6,7,0,1,2]
Output: 0
```

## Solution

```python
class Solution(object):
    def findMin(self, nums):
        """
        >>> nums = [4, 5, 6, 7, 0, 1, 2]
        >>> Solution().findMin(nums)
        0
        >>> nums = [3, 4, 5, 1, 2]
        >>> Solution().findMin(nums)
        1
        >>> nums = [2, 1]
        >>> Solution().findMin(nums)
        1
        """
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mi = (lo+hi)/2
            if nums[mi] <= nums[hi]:
                hi = mi
            elif nums[mi] >= nums[lo]:
                lo = mi + 1

        return nums[lo]
```
