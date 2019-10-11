---
tags: [2019/11/08, leetcode/594]
title: Longest Harmonious Subsequence
created: '2019-09-07T08:52:42.907Z'
modified: '2019-10-08T11:35:50.952Z'
---

# Longest Harmonious Subsequence

We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

### Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].


## Note:
The length of the input array will not exceed 20,000.

## schedule

* [x] 0 2019/09/12
* [ ] 1 2019/09/13

## Solution

```python
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        kv = {}
        for num in nums:
            kv.setdefault(num, 0)
            kv[num] += 1
        res = 0
        for k, v in kv.items():
            if (k+1) in kv:
                res = max(res, kv[k] + kv[k+1])
        return res

```

## schedule

* [x] 0 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [x] 1 2019/09/23
* [x] 1 2019/10/08
* [ ] 1 2019/11/08
