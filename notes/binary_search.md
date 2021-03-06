---
tags: [binary search/1]
title: Binary Search
created: '2019-08-02T05:39:13.642Z'
modified: '2019-08-03T04:54:57.268Z'
---

# Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


### Example 1:

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

### Example 2:

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```


> You may assume that all elements in nums are unique.
> n will be in the range [1, 10000].
> The value of each element in nums will be in the range [-9999, 9999].

## Solution

```python
class Solution(object):
    def search(self, nums, target):
        """
        >>> nums = [-1, 0, 3, 5, 9, 12]
        >>> target = 9
        >>> Solution().search(nums, target)
        4
        >>> nums = [-1, 0, 3, 5, 9, 12]
        >>> target = 2
        >>> Solution().search(nums, target)
        -1
        """
        n = len(nums)
        lo = 0
        hi = n-1
        while lo <= hi:
            mi = (lo+hi) / 2
            if target == nums[mi]:
                return mi
            elif target < nums[mi]:
                hi = mi - 1
            else:
                lo = mi + 1
        return -1
```
