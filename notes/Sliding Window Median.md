---
tags: [2020/01/07, leetcode/480, method/sliding-window]
title: Sliding Window Median
created: '2020-01-07T14:31:15.909Z'
modified: '2020-01-07T14:32:16.318Z'
---

# Sliding Window Median

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.

## Solution

```python
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = []
        for i in range(k-1):
            window.append(nums[i])
        
        res = []
        j = 0
        for i in range(k-1, len(nums)):
            window.append(nums[i])
            window.sort()
            
            res.append((window[k/2] + window[k-1-k/2])/2.0)
            
            window.remove(nums[j])
            j += 1
        return res
```

## refs

* [lc](https://leetcode.com/problems/sliding-window-median/)

## schedule

* [x] 2020/01/07
* [ ] 2020/01/08
