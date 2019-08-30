---
tags: [2019/08/30, leetcode/643]
title: Maximum Average Subarray I
created: '2019-08-30T14:46:54.026Z'
modified: '2019-08-30T14:47:11.155Z'
---

# Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

### Example 1:

```
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
```

> 1 <= k <= n <= 30,000.
> Elements of the given array will be in the range [-10,000, 10,000].

## Solution

```python
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        j = 0
        s = 0
        for j in range(k):
            s += nums[j]
        max_s = s
        i = 0
        for x in range(k, len(nums)):
            s = s - nums[i] + nums[x]
            i += 1
            max_s = max(max_s, s)
        return 1.0 * max_s / k
```
