---
tags: [2019/11/27, leetcode/665]
title: Non-decreasing Array
created: '2019-08-31T08:37:45.110Z'
modified: '2019-10-27T05:00:40.918Z'
---

# Non-decreasing Array

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

### Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

### Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

> The n belongs to [1, 10,000].

## Solution

```python
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i
        
        if p is None:
            return True
        if p == 0:
            return True
        if p == len(nums) - 2:
            return True
        if nums[p-1] <= nums[p+1]:
            return True
        if nums[p] <= nums[p+2]:
            return True
        return False
            
```


## schedule

* [x] 0 2019/10/01
* [x] 1 2019/10/02
* [x] 1 2019/10/05
* [x] 1 2019/10/12
* [x] 1 2019/10/27
* [ ] 1 2019/11/27
