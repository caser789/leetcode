---
tags: [2019/08/26, leetcode/169]
title: Majority Element
created: '2019-08-26T14:02:30.336Z'
modified: '2019-08-26T14:02:56.985Z'
---

# Majority Element


Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

### Example 1:

```
Input: [3,2,3]
Output: 3
```

### Example 2:

```
Input: [2,2,1,1,1,2,2]
Output: 2
```

## Solution

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums.sort()
        return nums[len(nums)/2]
```
