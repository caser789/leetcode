---
tags: [2019/08/29, hash, leetcode/1, method/search/hash, n-sum]
title: Two Sum
created: '2019-07-30T15:39:58.401Z'
modified: '2019-08-29T15:08:26.338Z'
---

# Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Solution

```py
class Solution(object):
    def twoSum(self, nums, target):
        """
        >>> s = Solution()
        >>> s.twoSum([2, 7, 11, 15], 9)
        [0, 1]
        """
        s = {}
        for i, num in enumerate(nums):
            if target - num in s:
                return [s[target - num], i]
            s[num] = i
```
