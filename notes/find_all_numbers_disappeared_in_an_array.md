---
tags: [2019/08/20, leetcode/448, method/index]
title: Find All Numbers Disappeared in an Array
created: '2019-08-20T14:04:47.267Z'
modified: '2019-08-20T14:13:00.074Z'
---

# Find All Numbers Disappeared in an Array


Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

### Example:

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```

## Solution

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res
```
