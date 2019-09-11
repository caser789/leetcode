---
tags: [application/array/intersection, application/array/n-array, data structure/array, data structure/map, leetcode/350, method/search/hash]
title: Intersection of Two Arrays II
created: '2019-07-30T15:48:53.870Z'
modified: '2019-09-07T08:29:28.592Z'
---

#  Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

### Example 1:

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

### Example 2:

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

#### Note:

* Each element in the result should appear as many times as it shows in both arrays.
* The result can be in any order.

### Follow up:

* What if the given array is already sorted? How would you optimize your algorithm?
* What if nums1's size is small compared to nums2's size? Which algorithm is better?
* What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

## Solution

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        >>> nums1 = [1, 2, 2, 1]
        >>> nums2 = [2, 2]
        >>> Solution().intersect(nums1, nums2)
        [2, 2]
        >>> nums1 = [4, 9, 5]
        >>> nums2 = [9, 4, 9, 8, 4]
        >>> Solution().intersect(nums1, nums2)
        [4, 9]
        """
        store = {}
        for num in nums1:
            store.setdefault(num, 0)
            store[num] += 1

        res = []
        for num in nums2:
            if num not in store:
                continue
            if store[num] == 0:
                continue
            res.append(num)
            store[num] -= 1
        return res
```
