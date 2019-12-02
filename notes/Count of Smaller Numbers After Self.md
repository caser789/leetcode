---
tags: [2019/11/13]
title: Count of Smaller Numbers After Self
created: '2019-11-13T02:11:01.534Z'
modified: '2019-11-13T04:45:56.136Z'
---

# Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

## Solution

```python
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        kv = {num: i for i, num in enumerate(sorted(set(nums)))}
        tree = Fenwick(len(kv))
        res = []
        for i in range(n-1, -1, -1):
            num = nums[i]
            j = kv[num]
            res.append(tree.sum(j))
            tree.update(j+1, 1)
        return res[::-1]


class Fenwick(object):
    def __init__(self, n):
        self.nums = [0] * (n+1)

    def update(self, i, val):
        while i < len(self.nums):
            self.nums[i] += val
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.nums[i]
            i -= i & -i
        return s

    def rsq(self, i, j):
        return self.sum(j) - self.sum(i-1)


```

## refs

* [lc](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)


