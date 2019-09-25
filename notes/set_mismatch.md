---
tags: [2019/10/08, leetcode/645]
title: Set Mismatch
created: '2019-09-07T08:54:10.509Z'
modified: '2019-09-23T14:17:53.749Z'
---

# Set Mismatch

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

### Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

## Note:

The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

## Solution

### O(lgn)

```python
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        a = None
        b = None
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                a = nums[i]
                break
        b = (1+n) * n / 2 - sum(nums) + a
        return [a, b]
```

### O(n)

```python
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Input: nums = [1,2,2,4]
        Output: [2,3]
        """
        n = len(nums)
        lst = range(1, n+1)

        res = []
        for num in nums:
            i = abs(num) - 1
            if lst[i] < 0:
                res.append(i+1)
            else:
                lst[i] = -lst[i]
        for i, v in enumerate(lst):
            if v > 0:
                res.append(i+1)
        return res
```

## schedule

* [x] 0 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [x] 1 2019/09/23
* [ ] 1 2019/10/08
