---
tags: [2019/11/03, leetcode/41, method/index]
title: First Missing Positive
created: '2019-11-02T04:53:28.098Z'
modified: '2019-11-02T04:55:04.825Z'
---

#  First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

## Solution

```python
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        
        for i in range(n):
            j = nums[i] % n
            nums[j] += n
        
        for i in range(1, n):
            if nums[i] < n:
                return i
        
        return n
        
```

## Schedule

* [x] 2019/11/02
* [ ] 2019/11/03

## refs

* [lc](https://leetcode.com/problems/first-missing-positive/)
