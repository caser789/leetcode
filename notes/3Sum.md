---
tags: [2019/11/03, leetcode/15]
title: 3Sum
created: '2019-11-02T02:42:36.341Z'
modified: '2019-11-02T02:43:56.385Z'
---

# 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


## Solution

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if i == 0 or nums[i] != nums[i-1]:
                lo = i + 1
                hi = n - 1
                s = -nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == s:
                        res.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < s:
                        lo += 1
                    else:
                        hi -= 1
        
        return res
```

## schedule

* [x] 2019/11/02
* [ ] 2019/11/03

## refs

* [lc](https://leetcode.com/problems/3sum/)
