---
tags: [binary search/2, template]
title: binary search template 1
created: '2019-08-02T05:36:25.313Z'
modified: '2019-08-02T05:54:07.344Z'
---

# binary search template 1


```python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
```

