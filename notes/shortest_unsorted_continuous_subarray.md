---
tags: [2019/09/30, leetcode/581, TODO]
title: Shortest Unsorted Continuous Subarray
created: '2019-08-31T08:34:12.401Z'
modified: '2019-09-24T15:21:31.129Z'
---

# Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

### Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

> Then length of the input array is in range [1, 10,000].
> The input array may contain duplicates, so ascending order here means <=.


## Solution

```python
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```
