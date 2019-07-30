---
tags: [set]
title: Intersection of Two Arrays
created: '2019-07-30T15:15:35.478Z'
modified: '2019-07-30T15:22:04.644Z'
---

# Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

### Example 1:

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

### Example 2:

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

> Each element in the result must be unique.
> The result can be in any order.

## Solution

```py
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        >>> s = Solution()
        >>> s.intersection([1, 2, 2, 1], [2, 2])
        [2]
        >>> s = Solution()
        >>> s.intersection([4, 9, 5], [9, 4, 9, 8, 4])
        [9, 4]
        """
        s1 = set(nums1)
        s2 = set()
        for num in nums2:
            if num in s1:
                s2.add(num)
        return list(s2)
```
