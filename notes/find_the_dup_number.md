---
title: Find the Duplicate Number
created: '2019-08-03T15:42:38.548Z'
modified: '2019-08-03T15:42:59.635Z'
---

# Find the Duplicate Number


Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

### Example 1:

```
Input: [1,3,4,2,2]
Output: 2
```

### Example 2:

```
Input: [3,1,3,4,2]
Output: 3
```

> You must not modify the array (assume the array is read only).
> You must use only constant, O(1) extra space.
> Your runtime complexity should be less than O(n2).
> There is only one duplicate number in the array, but it could be repeated more than once.


## Solution

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        >>> nums = [1, 3, 4, 2, 2]
        >>> Solution().findDuplicate(nums)
        2
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
```
