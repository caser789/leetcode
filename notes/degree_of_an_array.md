---
tags: [2019/08/28, data structure/map, leetcode/697, method/search/hash]
title: Degree of an Array
created: '2019-08-28T15:16:00.200Z'
modified: '2019-08-28T15:25:58.658Z'
---

# Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

### Example 1:

Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

### Example 2:

Input: [1,2,2,3,1,4,2]
Output: 6


> nums.length will be between 1 and 50,000.
> nums[i] will be an integer between 0 and 49,999.

## Solution


### Intuition

```python
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        start = {}
        end = {}
        cnt = {}
        max_cnt = 0
        for i, num in enumerate(nums):
            if num not in start:
                start[num] = i
            else:
                end[num] = i
            cnt.setdefault(num, 0)
            cnt[num] += 1
            max_cnt = max(max_cnt, cnt[num])
        if max_cnt == 1:
            return 1

        min_range = 999999999
        for num, c in cnt.items():
            if c == max_cnt:
                min_range = min(min_range, end[num]-start[num]+1)
        return min_range
```
