---
tags: [2019/12/04, leetcode/493]
title: Reverse Pairs
created: '2019-12-05T23:52:32.210Z'
modified: '2019-12-06T00:14:40.650Z'
---

# Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

## Solution

### brute force

```python
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > 2 * nums[j]:
                    cnt += 1
        return cnt
```

### BST

```python
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tree = BST()
        n = len(nums)
        cnt = 0
        for i in range(n):
            cnt += tree.search(nums[i]*2+1)
            head = tree.insert(nums[i])
            
        return cnt
    
class Node(object):
    
    def __init__(self, val):
        self.count_ge = 1
        self.left = None
        self.right = None
        self.val = val
        
        
class BST(object):

    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if node is None:
            return Node(val)
        
        if node.val == val:
            node.count_ge += 1
        elif val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.count_ge += 1
            node.right = self._insert(node.right, val)
        return node
    
    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if node is None:
            return 0
        
        if node.val == val:
            return node.count_ge
        
        if val < node.val:
            return node.count_ge + self._search(node.left, val)
        
        return self._search(node.right, val)


    
```

## refs

* [lc](https://leetcode.com/problems/reverse-pairs/)
* [solution](https://leetcode.com/problems/reverse-pairs/solution/)

