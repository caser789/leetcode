---
tags: [2019/09/15, leetcode/238, method/direction]
title: Product of Array Except Self
created: '2019-09-04T14:35:39.784Z'
modified: '2019-09-08T11:49:21.492Z'
---

# Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

### Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

> Note: Please solve it without division and in O(n).

## Follow up:

Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## Solution

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        s = 1
        left = [1] * n
        for i in range(n-1):
            s *= nums[i]
            left[i+1] = s

        s = 1
        right = [1] * n
        for i in range(n-1, 0, -1):
            s *= nums[i]
            right[i-1] = s

        for i in range(n):
            nums[i] = left[i] * right[i]
        return nums
```


## schedule

* [x] 0 2019/09/04
* [x] 1 2019/09/05
* [x] 1 2019/09/08
* [ ] 1 2019/09/15
