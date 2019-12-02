---
tags: [2019/11/25, leetcode/506]
title: Relative Ranks
created: '2019-09-24T15:17:24.600Z'
modified: '2019-10-25T04:53:23.963Z'
---

# Relative Ranks

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

## Solution

```python
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        x = sorted(nums)
        kv = {}
        for i, num in enumerate(x[::-1]):
            if i == 0:
                kv[num] = 'Gold Medal'
            elif i == 1:
                kv[num] = 'Silver Medal'
            elif i == 2:
                kv[num] = 'Bronze Medal'
            else:
                kv[num] = str(i+1)
        
        return [kv[num] for num in nums]
```

## schedule

* [x] 0 2019/09/29
* [x] 1 2019/09/30
* [x] 1 2019/10/03
* [x] 1 2019/10/10
* [x] 1 2019/10/25
* [ ] 1 2019/11/25
