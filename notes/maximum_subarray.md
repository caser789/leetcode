---
tags: [2019/08/26, leetcode/53, method/divide and conquer, method/dp]
title: Maximum Subarray
created: '2019-08-26T14:25:58.235Z'
modified: '2019-08-26T15:01:41.513Z'
---

# Maximum Subarray


Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Example:

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

> If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Solution

### linear way

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -9999999999
        s = 0
        for num in nums:
            s += num
            max_sum = max(s, max_sum)
            if s <= 0:
                s = 0
        return max_sum
```

### dp

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0
        max_num = -999999
        for i, num in enumerate(nums):
            dp[i+1] = dp[i] + num if dp[i] > 0 else num
            max_num = max(max_num, dp[i+1])
        return max_num
```

### divide and conquer

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self._max_sub_array(nums, 0, n-1)

    def _max_sub_array(self, nums, lo, hi):
        if lo == hi:
            return nums[lo]
        m = (lo+hi)/2
        return max(
            self._max_sub_array(nums, lo, m),
            self._max_sub_array(nums, m+1, hi),
            self._crossing_sub_array(nums, lo, mi, hi),
        )

    def _crossing_sub_array(self, nums, lo, mi, hi):
        s = 0
        left_sum = -9999
        for i in range(m, lo-1, -1):
            s += nums[i]
            left_sum = max(left_sum, s)


        s = 0
        right_sum = -9999
        for i in range(m+1, hi+1):
            s += nums[i]
            right_sum = max(right_sum, s)

        return left_sum + right_sum
```
