---
tags: [2019/08/28, leetcode/283, method/2 pointers]
title: Move Zeroes
created: '2019-08-28T15:08:24.963Z'
modified: '2019-08-28T15:12:43.088Z'
---

# Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

### Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

### Note:

> You must do this in-place without making a copy of the array.
> Minimize the total number of operations.

## Solution

```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
```
