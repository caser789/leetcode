---
tags: [2019/08/28, application/array/status, leetcode/485]
title: Max Consecutive Ones
created: '2019-08-28T14:51:48.796Z'
modified: '2019-08-28T15:07:28.036Z'
---

# Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

### Example 1:

```
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
```

> The input array will only contain 0 and 1.
> The length of input array is a positive integer and will not exceed 10,000

## Solution

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        max_cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
        max_cnt = max(max_cnt, cnt)
        return max_cnt
```
