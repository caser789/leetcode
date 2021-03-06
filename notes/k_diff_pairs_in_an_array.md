---
tags: [2019/11/06, leetcode/532]
title: K-diff Pairs in an Array
created: '2019-08-31T08:35:43.192Z'
modified: '2019-10-22T15:04:44.952Z'
---

# K-diff Pairs in an Array

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

### Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

### Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

### Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

> The pairs (i, j) and (j, i) count as the same pair.
> The length of the array won't exceed 10,000.
> All the integers in the given input belong to the range: [-1e7, 1e7].

## Solution

```python
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        counter = {}
        for num in nums:
            counter.setdefault(num, 0)
            counter[num] += 1

        res = 0
        for i, cnt in counter.items():
            if k == 0:
                if cnt > 1:
                    res += 1
            else:
                if i + k in counter:
                    res += 1
        return res
```

## schedule

* [x] 0 2019/09/15
* [x] 1 2019/09/16
* [x] 1 2019/09/19
* [x] 1 2019/09/26
* [x] 1 2019/10/11
* [x] 1 2019/10/12
* [x] 1 2019/10/15
* [x] 1 2019/10/22
* [ ] 1 2019/11/06
