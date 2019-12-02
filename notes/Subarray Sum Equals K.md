---
tags: [2019/11/20, leetcode/560]
title: Subarray Sum Equals K
created: '2019-11-20T05:38:26.214Z'
modified: '2019-11-20T05:40:06.935Z'
---

# Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

## Solution

```
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        [1,1,1], k = 2
        """
        res = 0
        s = 0
        kv = {0: 1}
        for i in range(len(nums)):
            s += nums[i]
            if s - k in kv:
                res += kv[s-k]
            kv[s] = kv.get(s, 0) + 1
        return res

```

## refs

* [lc](https://leetcode.com/problems/subarray-sum-equals-k/)
* [dis](https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book)
