---
tags: [2019/12/04, data structure/binary-indexed-tree, leetcode/307]
title: Range Sum Query - Mutable
created: '2019-11-12T14:30:09.710Z'
modified: '2019-12-03T05:46:56.726Z'
---

# Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

## Solution

```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.tree = FenwickTree(len(nums))
        for i, num in enumerate(nums):
            self.tree.update(i+1, num)     

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        x = val - self.nums[i]
        self.nums[i] = val
        self.tree.update(i+1, x)        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.rsq(i+1, j+1)
    
class FenwickTree(object):
    def __init__(self, n):
        self.nums = [0] * (n+1)
    def update(self, i, num):
        while i < len(self.nums):
            self.nums[i] += num
            i += i & (-i)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.nums[i]
            i -= i & (-i)
        return s
    def rsq(self, i, j):
        return self.sum(j) - self.sum(i-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
```

### better

```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        
        self.nums = [0] * n
        self.sums = [0] * (n+1)
        
        for i in range(n):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        j = i + 1
        upd = val - self.nums[i]
        
        while j < len(self.sums):
            self.sums[j] += upd
            j += j & (-j)
        
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(j+1) - self.query(i)
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= i & (-i)
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
```

## refs

* [lc](https://leetcode.com/problems/range-sum-query-mutable/)

## schedule

* [x] 2019/12/03
* [ ] 2019/12/04
