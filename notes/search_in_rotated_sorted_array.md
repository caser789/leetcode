---
tags: [application/rotated array, application/sorted array/peak, method/search/binary/1, method/search/binary/2]
title: Search in Rotated Sorted Array
created: '2019-08-02T05:45:12.458Z'
modified: '2019-08-09T04:36:20.532Z'
---

# Search in Rotated Sorted Array


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

### Example 1:

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### Example 2:

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## Solution

```python
class Solution(object):
    def search(self, nums, target):
        """
        >>> nums = [4, 5, 6, 7, 0, 1, 2]
        >>> target = 0
        >>> Solution().search(nums, target)
        4
        >>> nums = [4, 5, 6, 7, 0, 1, 2]
        >>> target = 3
        >>> Solution().search(nums, target)
        -1
        >>> nums = [5, 1, 3]
        >>> target = 1
        >>> Solution().search(nums, target)
        1
        """
        rot_i = self.find_min_index(nums)
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mi = (lo+hi) / 2
            real_index = (mi + rot_i) % len(nums)
            if nums[real_index] == target:
                return real_index
            elif target < nums[real_index]:
                hi = mi - 1
            else:
                lo = mi + 1
        return -1

    def find_min_index(self, nums):
        # find the smallest number
        """
        >>> nums = [4, 5, 6, 7, 0, 1, 2]
        >>> Solution().find_min_index(nums)
        4
        >>> nums = [4, 5, 6, 7]
        >>> Solution().find_min_index(nums)
        0
        >>> nums = [3, 1]
        >>> Solution().find_min_index(nums)
        1
        >>> nums = [5, 1, 3]
        >>> Solution().find_min_index(nums)
        1
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mi = (lo+hi)/2
            if nums[mi] < nums[hi]:
                hi = mi
            elif nums[mi] >= nums[lo]:
                lo = mi + 1
        return lo
```
