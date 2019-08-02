---
tags: [duplicate, hash]
title: Contains Duplicate II
created: '2019-07-30T15:50:41.583Z'
modified: '2019-08-02T05:33:24.869Z'
---

# Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

### Example 1:

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

### Example 2:

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

### Example 3:

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Solution

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        >>> Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)
        True
        >>> Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)
        True
        >>> Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
        False
        """
        store = {}
        for i, num in enumerate(nums):
            if num not in store:
                store[num] = i
            else:
                if i - store[num] <= k:
                    return True
                store[num] = i
        return False

```
