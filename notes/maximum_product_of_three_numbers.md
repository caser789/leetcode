---
tags: [2019/08/29, leetcode/628]
title: Maximum Product of Three Numbers
created: '2019-08-29T14:23:28.125Z'
modified: '2019-08-29T14:25:41.848Z'
---

# Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

### Example 1:

```
Input: [1,2,3]
Output: 6
```

### Example 2:

```
Input: [1,2,3,4]
Output: 24
```

> The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
> Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

## Solution

```python
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = -1000
        i = j = 1000
        for num in nums:
            if num < i:
                j = i
                i = num
            elif num < j:
                j = num

            if num > a:
                a, b, c = num, a, b
            elif num > b:
                b, c = num, b
            elif num > c:
                c = num

        if i * j > b * c:
            return i * j * a
        return a * b * c
```
