---
tags: [2019/08/20, leetcode/268, method/math]
title: Missing Number
created: '2019-08-20T13:53:46.907Z'
modified: '2019-08-20T14:03:09.897Z'
---

# Missing Number


Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

### Example 1:

```
Input: [3,0,1]
Output: 2
```

### Example 2:

```
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

> Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

## Solution

```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n+0)*(n+1)/2 - sum(nums)
```
