---
title: Find Minimum in Rotated Sorted Array II
created: '2019-08-03T14:19:16.898Z'
modified: '2019-08-03T14:19:47.636Z'
---

# Find Minimum in Rotated Sorted Array II


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

### Example 1:

```
Input: [1,3,5]
Output: 1
```

### Example 2:

```
Input: [2,2,2,0,1]
Output: 0
```

> This is a follow up problem to Find Minimum in Rotated Sorted Array.
> Would allow duplicates affect the run-time complexity? How and why?


## Solution

```python
class Solution(object):
    def findMin(self, nums):
        """
        >>> nums = [1, 3, 5]
        >>> Solution().findMin(nums)
        1
        >>> nums = [2, 2, 2, 0, 1]
        >>> Solution().findMin(nums)
        0
        >>> nums = [3, 3, 1, 3]
        >>> Solution().findMin(nums)
        1
        >>> nums = [1, 3, 3]
        >>> Solution().findMin(nums)
        1
        """
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mi = (lo+hi)/2
            v = nums[mi]
            if v > nums[hi]:
                lo = mi + 1
            elif v < nums[hi]:
                hi = mi
            else:
                hi -= 1
        return nums[lo]
```
