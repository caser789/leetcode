---
tags: [data structure/set, leetcode/136, method/search/hash, number]
title: Single Number
created: '2019-07-30T15:07:46.850Z'
modified: '2019-09-07T08:23:45.727Z'
---

# Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.


> Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

### Example 1:

```
Input: [2,2,1]
Output: 1
```

### Example 2:

```
Input: [4,1,2,1,2]
Output: 4
```

## Solution

```py
class Solution(object):
    def singleNumber(self, nums):
        """
        >>> s = Solution()
        >>> s.singleNumber([2, 2, 1])
        1
        >>> s = Solution()
        >>> s.singleNumber([4, 1, 2, 1, 2])
        4
        """
        n = 0
        s = set()
        for num in nums:
            if num in s:
                n -= num
            else:
                n += num
                s.add(num)
        return n
```
