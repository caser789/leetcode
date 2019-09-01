---
tags: [2019/08/31, application/array/neighbour, leetcode/605]
title: Can Place Flowers
created: '2019-08-31T08:32:27.879Z'
modified: '2019-09-01T10:17:27.239Z'
---

# Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

### Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

### Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

> The input array won't violate no-adjacent-flowers rule.
> The input array size is in the range of [1, 20000].
> n is a non-negative integer which won't exceed the input array size.


## Solution


### left and right list

```python
class Solution(object):
    def canPlaceFlowers(self, nums, m):
        """
        :type flowerbed: List[int]
        :type m: int
        :rtype: bool
        """
        n = len(nums)

        left = [n*2] * n
        right = [n*2] * n

        for i in range(n):
            if nums[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1

        for i in range(n-1, -1, -1):
            if nums[i] == 1:
                right[i] = 0
            elif i < n - 1:
                right[i] = right[i+1] + 1
        cnt = 0
        for i in range(n):
            if left[i] != 0 and left[i] % 2 == 0 and right[i] != 0 and right[i] > 1:
                cnt += 1

        return cnt >= m
```

### update input

```python
class Solution(object):
    def canPlaceFlowers(self, nums, m):
        """
        :type flowerbed: List[int]
        :type m: int
        :rtype: bool
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            if nums[i] == 0 and (i == 0 or nums[i-1] == 0) and (i == n-1 or nums[i+1] == 0):
                nums[i] = 1
                cnt += 1
        return cnt >= m
```

### quick update input

```python
class Solution(object):
    def canPlaceFlowers(self, nums, m):
        """
        :type flowerbed: List[int]
        :type m: int
        :rtype: bool
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            if nums[i] == 0 and (i == 0 or nums[i-1] == 0) and (i == n-1 or nums[i+1] == 0):
                nums[i] = 1
                cnt += 1

            if cnt >= m:
                return True
        return  False
```
