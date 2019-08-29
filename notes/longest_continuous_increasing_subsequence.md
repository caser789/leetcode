---
tags: [2019/08/29, leetcode/674, method/sliding window]
title: Longest Continuous Increasing Subsequence
created: '2019-08-29T14:59:53.217Z'
modified: '2019-08-29T15:06:40.746Z'
---

# Longest Continuous Increasing Subsequence

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

### Example 1:

```
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
```

### Example 2:

```
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
```

> Length of the array will not exceed 10,000.


## Solution

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len = 0
        n = len(nums)
        cnt = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                max_len = max(max_len, cnt)
                cnt = 1
        max_len = max(max_len, cnt)
        return max_len
```
